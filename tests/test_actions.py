from unittest import mock

from directory_forms_api_client import actions, client


def test_email_action_mixin_action_class(settings):
    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.EmailAction(
        recipients=['test@example.com'],
        client=mock_client,
        subject='a subject',
        reply_to=['reply_to@example.com'],
    )

    action.save({'field_one': 'value one', 'field_two': 'value two'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'field_one': 'value one', 'field_two': 'value two'},
        'meta': {
            'action_name': 'email',
            'recipients': ['test@example.com'],
            'reply_to': ['reply_to@example.com'],
            'subject': 'a subject',
            'namespace': settings.DIRECTORY_FORMS_API_NAMESPACE
        }
    })


def test_zendesk_action_mixin_action_class(settings):

    mock_client = mock.Mock(spec_set=client.APIFormsClient)
    action = actions.ZendeskAction(
        client=mock_client,
        subject='a subject',
        full_name='jim example',
        email_address='jim@example.com',
    )

    action.save({'requester_email': 'a@foo.com', 'field_two': 'value two'})

    assert mock_client.submit_generic.call_count == 1
    assert mock_client.submit_generic.call_args == mock.call({
        'data': {'requester_email': 'a@foo.com', 'field_two': 'value two'},
        'meta': {
            'action_name': 'zendesk',
            'subject': 'a subject',
            'full_name': 'jim example',
            'email_address': 'jim@example.com',
            'namespace': settings.DIRECTORY_FORMS_API_NAMESPACE
        }
    })
