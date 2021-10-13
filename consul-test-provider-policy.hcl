service "consul-test-provider" {
  policy = "write"
}

service "consul-test-provider-sidecar-proxy" {
  policy = "write"
}

service_prefix "" {
  policy = "read"
}

node_prefix "" {
  policy = "read"
}
