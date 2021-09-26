class SerializerMixin(object):
    def get_serializer_class(self):
        return self.serializers.get(self.action)