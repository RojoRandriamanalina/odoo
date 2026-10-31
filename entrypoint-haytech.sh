#!/bin/sh
# Mot de passe maître Odoo fourni par l'environnement (variable Coolify ADMIN_PASSWD), jamais écrit dans git
if [ -n "$ADMIN_PASSWD" ] && ! grep -q '^admin_passwd' /etc/odoo/odoo.conf; then
    printf 'admin_passwd = %s\n' "$ADMIN_PASSWD" >> /etc/odoo/odoo.conf
fi
exec /entrypoint.sh "$@"
