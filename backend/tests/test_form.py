from django.test import SimpleTestCase
from backend.app.forms import PostForm
class TestForm(SimpleTestCase):
    def test_form_valid_data(self):
        form = PostForm(data={
            'text': 'Как дела'
        })

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = PostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)