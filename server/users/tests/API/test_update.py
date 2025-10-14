from django.contrib.auth import get_user_model
class TestUpdate:
    def test_patch_user(self, auth_client):
        client, user = auth_client

        response = client.patch(
            f"/users/api/v1/{user.id}/",
            data={"full_name": "Patched Name"},
            format="json"
        )

        assert response.status_code == 200
        assert response.json()['full_name'] == "Patched Name"

    def test_put_user(self, auth_client):
        client, user = auth_client

        response = client.put(
            f"/users/api/v1/{user.id}/",
            data={
                "email":user.email,
                "full_name": "Puted Name",
                "is_active": True,
                "is_staff": False,
                "is_superuser": False
            },
            format="json"
        )
        User = get_user_model()
        assert User.objects.filter(id=user.id).exists()
