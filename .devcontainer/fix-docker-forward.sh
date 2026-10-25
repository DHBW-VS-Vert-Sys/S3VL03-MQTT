#!/usr/bin/env bash
# Legacy iptables FORWARD policy is DROP after dockerd starts and blocks bridged container-to-container traffic.
set -u

for _ in $(seq 1 30); do
  docker info >/dev/null 2>&1 && break
  sleep 1
done

sudo iptables-legacy -P FORWARD ACCEPT
