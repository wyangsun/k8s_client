from kubernetes import client, config

from st2common.runners.base_action import Action

class get_pods(Action):
    def run(
            self,
            namespace=None,
            labels=None):

        # Configs can be set in Configuration class directly or using helper utility
        config.load_kube_config()
        v1 = client.CoreV1Api()
        ret = v1.list_namespaced_pod(namespace, watch=False)
        return (True, ret.items)