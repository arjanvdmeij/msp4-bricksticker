from django.test import TestCase
from .models import FAQ

# Create your tests here.

class TestInfoPages(TestCase):
    print('Running Info Page Tests')
    def test_get_about_page(self):
        page = self.client.get('/info/about/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'about.html')
    
    def test_get_privacy_page(self):
        page = self.client.get('/info/privacy/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'privacy.html')
    
    def test_get_returns_page(self):
        page = self.client.get('/info/returns/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'returns.html')
    
    def test_get_terms_and_conditions_page(self):
        page = self.client.get('/info/terms/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'terms_and_conditions.html')
    
    def test_faq_model_str(self):
        faq = FAQ(
            question = 'words?', 
            answer = 'yes, multiple..'
            )
        faq.save()
        faq = FAQ.objects.filter(question='words?')
        answer = faq[0].answer
        self.assertIn('multiple',answer)