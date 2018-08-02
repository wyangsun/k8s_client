from kubernetes import client, config

from st2common.runners.base_action import Action

class del_pod(Action):
    def run(
            self,
            namespace=None,
            pod_name=None):

        # Configs can be set in Configuration class directly or using helper utility
        config.load_kube_config()
        v1 = client.CoreV1Api()
        body = client.V1DeleteOptions()
        api_reponse = v1.delete_namespaced_pod(pod_name, namespace, body)
        return (True, api_reponse)