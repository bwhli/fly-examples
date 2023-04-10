# Fly Python Samples

## fly-litestar-example

This example demonstrates how to configure a Litestar API for Fly.io's Machines platform. Fly Machines automatically respond and wake up to incoming requests, and shut down (scale to zero) when the host application exits. This model is ideal for stateless FaaS (function-as-a-service) use cases that would benefit from putting VMs to sleep when they're not active.

This example uses the Litestar features below to implement "scale to zero".

* `before_request_handler` records the timestamp before each request is processed.
* `after_startup_handler` starts a while loop that sends a SIGTERM signal once the shutdown timeout has been exceeded. 

### How to Use

1. `fly launch --force-machines`
2. `fly secrets set SHUTDOWN_TIMEOUT=60` (feel free to change the duration as needed)
3. `fly deploy`