# encoding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from manozodynas.testutils import StatefulTesting


class IndexTestCase(StatefulTesting):
    def test_index_page(self):
        self.open(reverse('index'))
        self.assertStatusCode(200)


class WordTestCase(StatefulTesting):
    def test_new_word_page(self):
        self.open(reverse('new_word'))
        self.selectForm('#new_word')
        self.assertStatusCode(200)
        self.submitForm({'definition': 'Python'})
        self.assertStatusCode(302)
        self.state['response'].content
        self.open(reverse('words'))
        self.assertTrue('Python' in self.state['response'].content)
        

