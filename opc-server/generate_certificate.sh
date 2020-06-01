openssl genrsa -out key.pem 2048
openssl req -x509 -days 365 -new -out certificate.pem -key key.pem -config ssl.conf
