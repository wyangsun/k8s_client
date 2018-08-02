from kubernetes import client, config

from st2common.runners.base_action import Action

class deployment_scale(Action):
    def run(
            self,
            namespace=None,
            number=None,
            min=None,
            max=None,
            deploy_name=None):

        # Configs can be set in Configuration class directly or using helper utility
        config.load_kube_config()
        v1 = client.AppsV1Api()
        body = read_namespaced_deployment_scale(deploy_name, namespace, pretty=pretty)
        return (True, body)
        #if number > min && number < max:
        #    body.number = number
        #else:
        #	return (False, 'bad number')
        #api_reponse = v1.patch_namespaced_deployment_scale(deploy_name, namespace, body, pretty=pretty)
        #return (True, api_reponse)