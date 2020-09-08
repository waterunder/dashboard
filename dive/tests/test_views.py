from dive.factories import DiveFactory, UserFactory
from dive.views import DiveCreate, DiveDelete, DiveDetailView, DiveListView, DiveUpdate
from django.test import TestCase
from django.urls import resolve, reverse


# Create your tests here.
class DiveListTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.dive = DiveFactory(created_by=self.user)

    def test_dive_list_view_resolves_divelistview(self):
        view = resolve(reverse('dive_list'))
        self.assertEqual(view.func.__name__, DiveListView.as_view().__name__)

    def test_dive_list_redirects_for_logged_out_user(self):
        response = self.client.get(reverse('dive_list'))
        no_response = self.client.get('/dive_list/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'dive/dive_list.html')
        self.assertEqual(no_response.status_code, 404)

    def test_dive_list_works_for_logged_in_user(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('dive_list'))
        no_response = self.client.get('/dive_list/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dive/dive_list.html')
        self.assertContains(response, 'Dives')
        self.assertContains(response, 'Log Book')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_dive_list_view_shows_dives_for_logged_in_user_only(self):
        pass


class DiveDetailTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.dive = DiveFactory(created_by=self.user)

    def test_dive_detail_view_resolves_divedetailview(self):
        view = resolve(self.dive.get_absolute_url())
        self.assertEqual(view.func.__name__, DiveDetailView.as_view().__name__)

    def test_dive_detail_redirects_for_logged_out_user(self):
        response = self.client.get(self.dive.get_absolute_url())
        no_response = self.client.get('/dive/123456/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'dive/dive_detail.html')
        self.assertEqual(no_response.status_code, 404)

    def test_dive_detail_works_for_logged_in_user(self):
        self.client.force_login(self.user)

        response = self.client.get(self.dive.get_absolute_url())
        no_response = self.client.get('/dive/123456/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dive/dive_detail.html')
        self.assertContains(response, 'Log Book')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)


class DiveCreateTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.dive = DiveFactory(created_by=self.user)

    def test_dive_create_resolves_divecreateview(self):
        view = resolve(reverse('dive_create'))
        self.assertEqual(view.func.__name__, DiveCreate.as_view().__name__)

    def test_dive_create_redirects_for_logged_out_user(self):
        response = self.client.get(reverse('dive_create'))
        no_response = self.client.get('/dive_create/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'dive/dive_form.html')
        self.assertEqual(no_response.status_code, 404)

    def test_dive_create_works_for_logged_in_user(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('dive_create'))
        no_response = self.client.get('/dive_create/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dive/dive_form.html')
        self.assertContains(response, 'Log Book')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)


class DiveUpdateTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.dive = DiveFactory(created_by=self.user)

    def test_dive_update_works_for_user_who_created_the_dive(self):
        pass

    def test_dive_update_redirects_for_user_who_did_not_create_the_dive(self):
        pass

    def test_dive_update_works_for_super_user(self):
        pass

    def test_dive_update_resolves_diveupdateview(self):
        view = resolve(self.dive.get_update_url())
        self.assertEqual(view.func.__name__, DiveUpdate.as_view().__name__)

    def test_dive_update_redirects_for_logged_out_user(self):
        response = self.client.get(self.dive.get_update_url())
        no_response = self.client.get('/dive/123456/update/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'dive/dive_update_form.html')
        self.assertEqual(no_response.status_code, 404)

    def test_dive_update_works_for_logged_in_user(self):
        self.client.force_login(self.user)

        response = self.client.get(self.dive.get_update_url())
        no_response = self.client.get('/dive/123456/update/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dive/dive_update_form.html')
        self.assertContains(response, 'Log Book')
        self.assertContains(response, 'Update')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)


class DiveDeleteTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.dive = DiveFactory(created_by=self.user)

    def test_dive_delete_works_for_logged_in_user(self):
        self.client.force_login(self.user)

        response = self.client.get(self.dive.get_delete_url())
        no_response = self.client.get('/dive/123456/delete/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dive/dive_confirm_delete.html')
        self.assertContains(response, 'Log Book')
        self.assertContains(response, 'Delete')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_dive_delete_redirects_for_logged_out_user(self):
        response = self.client.get(self.dive.get_delete_url())
        no_response = self.client.get('/dive/123456/delete/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'dive/dive_confirm_delete.html')
        self.assertEqual(no_response.status_code, 404)

    def test_dive_delete_works_for_super_user(self):
        pass

    def test_dive_delete_works_for_user_who_created_the_dive(self):
        pass

    def test_dive_delete_redirects_for_user_who_did_not_create_the_dive(self):
        pass

    def test_dive_delete_resolves_divedeleteview(self):
        view = resolve(self.dive.get_delete_url())
        self.assertEqual(view.func.__name__, DiveDelete.as_view().__name__)
