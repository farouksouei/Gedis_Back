from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import OrganizationDetails
from .serializer import OrganizationDetailsSerializer


# Create your views here.
class OrganizationDetailViewSet(viewsets.ModelViewSet):
    queryset = OrganizationDetails.objects.all()
    serializer_class = OrganizationDetailsSerializer
    permission_classes = []

    @action(detail=False, methods=['post'], url_path='add-organization-detail')
    def add_organization_detail(self, request):
        organization_detail_serializer = OrganizationDetailsSerializer(data=request.data)
        if organization_detail_serializer.is_valid():
            organization_detail_serializer.save()
            return Response({"success": "Organization detail added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Organization detail not added"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='get-organization-detail')
    def get_organization_detail(self, request):
        organization_detail = OrganizationDetails.objects.all()
        organization_detail_serializer = OrganizationDetailsSerializer(organization_detail, many=True)
        return Response(organization_detail_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='get-organization-detail-by-id')
    def get_organization_detail_by_id(self, request):
        organization_detail = OrganizationDetails.objects.get(id=request.GET['id'])
        organization_detail_serializer = OrganizationDetailsSerializer(organization_detail)
        return Response(organization_detail_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'], url_path='update-organization-detail')
    def update_organization_detail(self, request):
        organization_detail = OrganizationDetails.objects.get(id=request.data['id'])
        organization_detail_serializer = OrganizationDetailsSerializer(organization_detail, data=request.data)
        if organization_detail_serializer.is_valid():
            organization_detail_serializer.save()
            return Response({"success": "Organization detail updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Organization detail not updated"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='delete-organization-detail')
    def delete_organization_detail(self, request):
        organization_detail = OrganizationDetails.objects.get(id=request.GET['id'])
        organization_detail.delete()
        return Response({"success": "Organization detail deleted successfully"}, status=status.HTTP_200_OK)
