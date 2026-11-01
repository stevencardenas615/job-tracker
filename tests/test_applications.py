

def test_create_application_defaults_saved(client, auth_headers):
    r = client.post("/applications", json={"company": "Amazon", "role": "SWE", "location": "San Diego, CA","url": "www.Amazon.com"}, headers=auth_headers)
    assert r.status_code == 201
    assert r.json()["status"] == "saved"