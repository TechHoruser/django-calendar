
## Creación entorno Virtual

#### Comandos a seguir:

```bash
cd vm
vagrant up
cd ..
cp vm/.vagrant/machines/default/virtualbox/private_key ansible
cd ansible
cp ansible.cfg.default ansible.cfg
ansible-playbook -i hosts playbook.yml
``` 

