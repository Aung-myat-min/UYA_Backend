from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactMessageSerializer
from django.urls import reverse

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Send email to organization
            send_mail(
                subject=f"[UYA Website] {contact.subject}",
                message=f"Name: {contact.sender}\nEmail: {contact.email}\n\n{contact.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ORG_EMAIL],
            )

            # Auto-reply to sender
            send_mail(
                subject="We received your message – UYA",
                message="Thank you for contacting United Youth Association of Burma. We will get back to you shortly.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
            )

            return Response({
                "meta": {
                    "message": "Message received successfully",
                    "status_code": status.HTTP_201_CREATED
                },
                "data": ContactMessageSerializer(contact).data,
                "links": {
                    "self": request.build_absolute_uri(),
                }
            }, status=status.HTTP_201_CREATED)

        return Response({
            "meta": {
                "message": "Message submission failed",
                "status_code": status.HTTP_400_BAD_REQUEST
            },
            "data": None,
            "errors": serializer.errors,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_400_BAD_REQUEST)

