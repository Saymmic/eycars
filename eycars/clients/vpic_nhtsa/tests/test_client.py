from eycars.clients.vpic_nhtsa.clients import client as vpic_client


def test_test_a():
    models = vpic_client.models_for_make.list("honda")
    print(models)
