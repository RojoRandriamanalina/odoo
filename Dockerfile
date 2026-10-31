FROM odoo:20.0
USER root
COPY addons /mnt/extra-addons
COPY odoo.conf /etc/odoo/odoo.conf
COPY entrypoint-haytech.sh /entrypoint-haytech.sh
RUN chown -R odoo /mnt/extra-addons /etc/odoo/odoo.conf && chmod +x /entrypoint-haytech.sh
USER odoo
ENTRYPOINT ["/entrypoint-haytech.sh"]
CMD ["odoo"]
