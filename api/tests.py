from unittest import mock

from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase

from core.models import EducationalOpportunity


class EducationalOpportunityCreateApiTests(APITestCase):
    @mock.patch('random.randint')
    def test_create(self, randint_mock):
        randint_mock.return_value = 50

        path = reverse_lazy('create_random_educational_opportunities')
        data = {
            'count': 100,
            'activity': 'test_activity'
        }
        res = self.client.post(path, data=data)
        self.assertEqual(res.status_code, 201)

        self.assertEqual(EducationalOpportunity.objects.count(), 100)
        self.assertEqual(
            EducationalOpportunity.objects.filter(activity='test_activity', scales=[50] * 6).count(), 100)


class EducationalOpportunityViewSetTests(APITestCase):
    def test_list(self):
        educational_opportunity_1 = EducationalOpportunity.objects.create_random('test_activity_1')
        educational_opportunity_2 = EducationalOpportunity.objects.create_random('test_activity_2')
        path = reverse_lazy('educationalopportunity-list')
        res = self.client.get(path)
        self.assertEqual(res.status_code, 200)
        data = res.data
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['id'], str(educational_opportunity_1.id))
        self.assertEqual(data[0]['activity'], 'test_activity_1')
        self.assertEqual(data[0]['scales'], educational_opportunity_1.scales)
        self.assertEqual(data[1]['id'], str(educational_opportunity_2.id))
        self.assertEqual(data[1]['activity'], 'test_activity_2')
        self.assertEqual(data[1]['scales'], educational_opportunity_2.scales)

    def test_list_filter(self):
        EducationalOpportunity.objects.create_random('test_activity_1')
        educational_opportunity = EducationalOpportunity.objects.create_random('test_activity_2')
        path = reverse_lazy('educationalopportunity-list')
        res = self.client.get(path, data={'activity': 'test_activity_2'})
        self.assertEqual(res.status_code, 200)
        data = res.data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], str(educational_opportunity.id))
        self.assertEqual(data[0]['activity'], 'test_activity_2')
        self.assertEqual(data[0]['scales'], educational_opportunity.scales)

    def test_list_filter_empty(self):
        EducationalOpportunity.objects.create_random('test_activity')
        path = reverse_lazy('educationalopportunity-list')
        res = self.client.get(path, data={'activity': 'test_activity_1'})
        self.assertEqual(res.status_code, 200)
        data = res.data
        self.assertEqual(len(data), 0)

    def test_retrieve(self):
        EducationalOpportunity.objects.create_random('test_activity_1')
        educational_opportunity = EducationalOpportunity.objects.create_random('test_activity')
        path = reverse_lazy('educationalopportunity-detail', kwargs={'pk': str(educational_opportunity.id)})
        res = self.client.get(path)
        self.assertEqual(res.status_code, 200)
        data = res.data
        self.assertEqual(data['id'], str(educational_opportunity.id))
        self.assertEqual(data['activity'], 'test_activity')
        self.assertEqual(data['scales'], educational_opportunity.scales)
