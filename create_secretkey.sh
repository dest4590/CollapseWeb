#!/bin/bash

if [ ! -f ".env" ]; then
    touch ".env"
fi

if ! grep -q "SECRET_KEY=" ".env"; then
    secret_key=$(tr -dc '[a-zA-Z0-9\-_!@#%^&*()_+{}|:?=' < /dev/urandom | head -c 50)
    echo "SECRET_KEY=$secret_key" >> ".env"
fi

