from rest_framework import serializers

from apps.products.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    serializer for model Category
    """
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.image)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    serializer for model Product
    """
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source='category',
        queryset=Category.objects.all()
    )
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return self.context['request'].build_absolute_uri(obj.image)

    class Meta:
        model = Product
        fields = '__all__'
