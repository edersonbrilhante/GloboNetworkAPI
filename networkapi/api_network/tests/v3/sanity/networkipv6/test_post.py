# -*- coding: utf-8 -*-
import json

from django.test.client import Client
from mock import patch

from networkapi.test.mock import MockPluginNetwork
from networkapi.test.test_case import NetworkApiTestCase


class NetworkIPv6PostSuccessTestCase(NetworkApiTestCase):

    fixtures = [
        'networkapi/system/fixtures/initial_variables.json',
        'networkapi/usuario/fixtures/initial_usuario.json',
        'networkapi/grupo/fixtures/initial_ugrupo.json',
        'networkapi/usuario/fixtures/initial_usuariogrupo.json',
        'networkapi/api_ogp/fixtures/initial_objecttype.json',
        'networkapi/api_ogp/fixtures/initial_objectgrouppermissiongeneral.json',
        'networkapi/grupo/fixtures/initial_permissions.json',
        'networkapi/grupo/fixtures/initial_permissoes_administrativas.json',

        'networkapi/vlan/fixtures/initial_tipo_rede.json',
        'networkapi/filter/fixtures/initial_filter.json',
        'networkapi/filterequiptype/fixtures/initial_filterequiptype.json',
        'networkapi/equipamento/fixtures/initial_tipo_equip.json',

        'networkapi/api_network/fixtures/sanity/initial_vrf.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_dc.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_envlog.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_gl3.json',
        'networkapi/api_network/fixtures/sanity/initial_environment.json',
        'networkapi/api_network/fixtures/sanity/initial_ipconfig.json',
        'networkapi/api_network/fixtures/sanity/initial_config_environment.json',
        'networkapi/api_network/fixtures/sanity/initial_vlan.json',
        'networkapi/api_network/fixtures/sanity/initial_networkipv6.json',
        'networkapi/api_network/fixtures/sanity/initial_ipv6.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_vip.json',
        'networkapi/api_network/fixtures/sanity/initial_vip_request_v6.json',
        'networkapi/api_network/fixtures/sanity/initial_env_env_vip.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments_env.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments_group.json',
        'networkapi/api_network/fixtures/sanity/initial_ipv6_eqpt.json',
        'networkapi/api_network/fixtures/sanity/initial_roteiros.json',
        'networkapi/api_network/fixtures/sanity/initial_equip_marca_model.json',

    ]

    json_path = 'api_network/tests/v3/sanity/networkipv6/json/%s'

    def setUp(self):
        self.client = Client()
        self.authorization = self.get_http_authorization('test')

    def tearDown(self):
        pass

    def test_try_create_netipv6_with_octs(self):
        """Test of success to create a Network IPv6 with octs."""

        name_file = self.json_path % 'post/net_with_octs.json'

        # Does POST request
        response = self.client.post(
            '/api/v3/networkv6/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.authorization)

        self.compare_status(201, response.status_code)

        get_url = '/api/v3/networkv6/%s/?kind=basic' % response.data[0]['id']

        name_file = self.json_path % 'get/basic/net_with_octs.json'

        response = self.client.get(
            get_url,
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        del response.data['networks'][0]['id']
        self.compare_json_lists(name_file, response.data['networks'])

    def test_try_create_netipv6_with_octs_and_env_vip(self):
        """Test of success to create a Network IPv6 with octs and Environment Vip."""

        name_file = self.json_path % 'post/net_with_octs_env_vip.json'

        # Does POST request
        response = self.client.post(
            '/api/v3/networkv6/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.authorization)

        self.compare_status(201, response.status_code)

        get_url = '/api/v3/networkv6/%s/?kind=basic' % response.data[0]['id']

        name_file = self.json_path % 'get/basic/net_with_octs_env_vip.json'

        response = self.client.get(
            get_url,
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        del response.data['networks'][0]['id']
        self.compare_json_lists(name_file, response.data['networks'])

    def test_try_create_netipv6_with_auto_alloc(self):
        """Test of success to create a Network IPv6 without octs."""

        name_file_post = 'api_network/tests/v3/sanity/networkipv6/json/post/net_without_octs.json'

        # Does POST request
        response = self.client.post(
            '/api/v3/networkv6/',
            data=json.dumps(self.load_json_file(name_file_post)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.authorization)

        self.compare_status(201, response.status_code)

        get_url = '/api/v3/networkv6/%s/?kind=basic' % response.data[0]['id']

        name_file = self.json_path % 'get/basic/net_without_octs.json'

        response = self.client.get(
            get_url,
            content_type='application/json',
            HTTP_AUTHORIZATION=self.get_http_authorization('test'))

        self.compare_status(200, response.status_code)

        del response.data['networks'][0]['id']
        self.compare_json_lists(name_file, response.data['networks'])


class NetworkIPv6DeploySuccessTestCase(NetworkApiTestCase):

    fixtures = [
        'networkapi/system/fixtures/initial_variables.json',
        'networkapi/usuario/fixtures/initial_usuario.json',
        'networkapi/grupo/fixtures/initial_ugrupo.json',
        'networkapi/usuario/fixtures/initial_usuariogrupo.json',
        'networkapi/api_ogp/fixtures/initial_objecttype.json',
        'networkapi/api_ogp/fixtures/initial_objectgrouppermissiongeneral.json',
        'networkapi/grupo/fixtures/initial_permissions.json',
        'networkapi/grupo/fixtures/initial_permissoes_administrativas.json',

        'networkapi/vlan/fixtures/initial_tipo_rede.json',
        'networkapi/filter/fixtures/initial_filter.json',
        'networkapi/filterequiptype/fixtures/initial_filterequiptype.json',
        'networkapi/equipamento/fixtures/initial_tipo_equip.json',

        'networkapi/api_network/fixtures/sanity/initial_vrf.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_dc.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_envlog.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_gl3.json',
        'networkapi/api_network/fixtures/sanity/initial_environment.json',
        'networkapi/api_network/fixtures/sanity/initial_ipconfig.json',
        'networkapi/api_network/fixtures/sanity/initial_config_environment.json',
        'networkapi/api_network/fixtures/sanity/initial_vlan.json',
        'networkapi/api_network/fixtures/sanity/initial_networkipv6.json',
        'networkapi/api_network/fixtures/sanity/initial_ipv6.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_vip.json',
        'networkapi/api_network/fixtures/sanity/initial_vip_request_v6.json',
        'networkapi/api_network/fixtures/sanity/initial_env_env_vip.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments_env.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments_group.json',
        'networkapi/api_network/fixtures/sanity/initial_ipv6_eqpt.json',
        'networkapi/api_network/fixtures/sanity/initial_roteiros.json',
        'networkapi/api_network/fixtures/sanity/initial_equip_marca_model.json',

    ]

    def setUp(self):
        self.client = Client()
        self.authorization = self.get_http_authorization('test')

    def tearDown(self):
        pass

    @patch('networkapi.plugins.factory.PluginFactory.factory')
    def test_try_deploy_inactive_netipv6(self, test_patch):
        """Test of error to deploy a inactive NetworkIPv6. NAPI should allow this request."""

        mock = MockPluginNetwork()
        mock.status(True)
        test_patch.return_value = mock

        url_post = '/api/v3/networkv6/deploy/3/'

        response = self.client.post(
            url_post,
            content_type='application/json',
            HTTP_AUTHORIZATION=self.authorization)

        self.compare_status(200, response.status_code)

        url_get = '/api/v3/networkv6/3/?fields=active'

        response = self.client.get(
            url_get,
            HTTP_AUTHORIZATION=self.authorization
        )

        self.compare_status(200, response.status_code)

        active = response.data['networks'][0]['active']
        self.compare_values(True, active)


class NetworkIPv6PostErrorTestCase(NetworkApiTestCase):

    fixtures = [
        'networkapi/system/fixtures/initial_variables.json',
        'networkapi/usuario/fixtures/initial_usuario.json',
        'networkapi/grupo/fixtures/initial_ugrupo.json',
        'networkapi/usuario/fixtures/initial_usuariogrupo.json',
        'networkapi/api_ogp/fixtures/initial_objecttype.json',
        'networkapi/api_ogp/fixtures/initial_objectgrouppermissiongeneral.json',
        'networkapi/grupo/fixtures/initial_permissions.json',
        'networkapi/grupo/fixtures/initial_permissoes_administrativas.json',

        'networkapi/vlan/fixtures/initial_tipo_rede.json',
        'networkapi/filter/fixtures/initial_filter.json',
        'networkapi/filterequiptype/fixtures/initial_filterequiptype.json',
        'networkapi/equipamento/fixtures/initial_tipo_equip.json',

        'networkapi/api_network/fixtures/sanity/initial_vrf.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_dc.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_envlog.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_gl3.json',
        'networkapi/api_network/fixtures/sanity/initial_environment.json',
        'networkapi/api_network/fixtures/sanity/initial_ipconfig.json',
        'networkapi/api_network/fixtures/sanity/initial_config_environment.json',
        'networkapi/api_network/fixtures/sanity/initial_vlan.json',
        'networkapi/api_network/fixtures/sanity/initial_networkipv6.json',
        'networkapi/api_network/fixtures/sanity/initial_ipv6.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_vip.json',
        'networkapi/api_network/fixtures/sanity/initial_vip_request_v6.json',
        'networkapi/api_network/fixtures/sanity/initial_env_env_vip.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments_env.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments_group.json',
        'networkapi/api_network/fixtures/sanity/initial_ipv6_eqpt.json',
        'networkapi/api_network/fixtures/sanity/initial_roteiros.json',
        'networkapi/api_network/fixtures/sanity/initial_equip_marca_model.json',

    ]

    json_path = 'api_network/tests/v3/sanity/networkipv6/json/%s'

    def setUp(self):
        self.client = Client()
        self.authorization = self.get_http_authorization('test')

    def tearDown(self):
        pass

    def test_try_create_netipv6_with_auto_alloc_in_full_env(self):
        """Test of error to create a Network IPv6 without octs in vlan of Environment with not available Network IPv6."""

        name_file = self.json_path % 'post/net_without_octs_full_env.json'

        # Does POST request
        response = self.client.post(
            '/api/v3/networkv6/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.authorization)

        self.compare_status(400, response.status_code)

        self.compare_values(
            'Unavailable address to create a NetworkIPv6.',
            response.data['detail'])

    def test_try_create_netipv6_with_octs_in_full_env(self):
        """Test of error to create a Network IPv6 with octs in vlan of Environment with not available Network IPv6."""

        name_file = self.json_path % 'post/net_with_octs_full_env.json'

        # Does POST request
        response = self.client.post(
            '/api/v3/networkv6/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.authorization)

        self.compare_status(400, response.status_code)

        msg = 'One of the equipment associated with the environment of this ' \
            'Vlan is also associated with other environment that has a ' \
            'network with the same track, add filters in environments if ' \
            'necessary. Your Network: fc00::/64, Network already created: ' \
            'fc00::/57'
        self.compare_values(msg, response.data['detail'])

    def test_try_create_netipv6_out_of_range_with_octs(self):
        """Test of error to create a Network IPv6 with octs out of range configuration defined in related Environment."""

        name_file = self.json_path % 'post/net_with_octs_out_of_range.json'

        # Does POST request
        response = self.client.post(
            '/api/v3/networkv6/',
            data=json.dumps(self.load_json_file(name_file)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.authorization)

        self.compare_status(400, response.status_code)

        msg = 'Network can not inserted in environment BE-TESTE-2 - TESTE - ' \
            'BALANCEAMENTO-POOL because network bebe:0000:0000:0000:0000:' \
            '0000:0000:0000/64 are in out of the range of allowed networks.'
        self.compare_values(msg, response.data['detail'])


class NetworkIPv6DeployErrorTestCase(NetworkApiTestCase):

    fixtures = [
        'networkapi/system/fixtures/initial_variables.json',
        'networkapi/usuario/fixtures/initial_usuario.json',
        'networkapi/grupo/fixtures/initial_ugrupo.json',
        'networkapi/usuario/fixtures/initial_usuariogrupo.json',
        'networkapi/api_ogp/fixtures/initial_objecttype.json',
        'networkapi/api_ogp/fixtures/initial_objectgrouppermissiongeneral.json',
        'networkapi/grupo/fixtures/initial_permissions.json',
        'networkapi/grupo/fixtures/initial_permissoes_administrativas.json',

        'networkapi/vlan/fixtures/initial_tipo_rede.json',
        'networkapi/filter/fixtures/initial_filter.json',
        'networkapi/filterequiptype/fixtures/initial_filterequiptype.json',
        'networkapi/equipamento/fixtures/initial_tipo_equip.json',

        'networkapi/api_network/fixtures/sanity/initial_vrf.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_dc.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_envlog.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_gl3.json',
        'networkapi/api_network/fixtures/sanity/initial_environment.json',
        'networkapi/api_network/fixtures/sanity/initial_ipconfig.json',
        'networkapi/api_network/fixtures/sanity/initial_config_environment.json',
        'networkapi/api_network/fixtures/sanity/initial_vlan.json',
        'networkapi/api_network/fixtures/sanity/initial_networkipv6.json',
        'networkapi/api_network/fixtures/sanity/initial_ipv6.json',
        'networkapi/api_network/fixtures/sanity/initial_environment_vip.json',
        'networkapi/api_network/fixtures/sanity/initial_vip_request_v6.json',
        'networkapi/api_network/fixtures/sanity/initial_env_env_vip.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments_env.json',
        'networkapi/api_network/fixtures/sanity/initial_equipments_group.json',
        'networkapi/api_network/fixtures/sanity/initial_ipv6_eqpt.json',
        'networkapi/api_network/fixtures/sanity/initial_roteiros.json',
        'networkapi/api_network/fixtures/sanity/initial_equip_marca_model.json',

    ]

    def setUp(self):
        self.client = Client()
        self.authorization = self.get_http_authorization('test')

    def tearDown(self):
        pass

    @patch('networkapi.plugins.factory.PluginFactory.factory')
    def test_try_deploy_active_netipv6(self, test_patch):
        """Test of error to deploy a active NetworkIPv6. NAPI should deny this request."""

        mock = MockPluginNetwork()
        mock.status(False)
        test_patch.return_value = mock

        url_post = '/api/v3/networkv6/deploy/1/'

        response = self.client.post(
            url_post,
            content_type='application/json',
            HTTP_AUTHORIZATION=self.authorization)

        self.compare_status(400, response.status_code)

        self.compare_values(
            'Already Active Network. Nothing to do.', response.data['detail'])

        url_get = '/api/v3/networkv6/1/?fields=active'

        response = self.client.get(
            url_get,
            HTTP_AUTHORIZATION=self.authorization
        )

        self.compare_status(200, response.status_code)

        active = response.data['networks'][0]['active']
        self.compare_values(True, active)