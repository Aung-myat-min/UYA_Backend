from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactMessageSerializer

class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Send email to organization
            send_mail(
                subject=f"[UYA Website] {contact.subject}",
                message=f"Name: {contact.name}\nEmail: {contact.email}\n\n{contact.message}",
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
                "status": "success",
                "data": ContactMessageSerializer(contact).data,
                "message": "Message received successfully"
            }, status=status.HTTP_201_CREATED)

        return Response({
            "status": "error",
            "errors": serializer.errors,
            "message": "Message submission failed"
        }, status=status.HTTP_400_BAD_REQUEST)

