from kubernetes import client, config

from st2common.runners.base_action import Action

class get_deployment(Action):
    def run(
            self,
            namespace=None):

        # Configs can be set in Configuration class directly or using helper utility
        config.load_kube_config()
        v1 = client.AppsV1Api()
        api_reponse = v1.list_namespaced_deployment(namespace)
        return (True, api_reponse)