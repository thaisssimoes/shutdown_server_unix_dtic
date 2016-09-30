import json
import paramiko
import sys
import traceback
import config

try:
    import interactive
except ImportError:
    from . import interactive
# setup logging
paramiko.util.log_to_file(config.log)

with open(config.documento_maquina) as arquivo:
    document = arquivo.read()
    documento_json = json.loads(document)
    for item in documento_json:
        # para cada uma das conexoes....
        try:
            ssh = paramiko.SSHClient()  # instanciando o objeto ssh
            # ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print('*** Connecting...')
            try:
                ssh.connect(hostname =item['hostname'], port=item['port'],username=item['username'], password=item['password'])
            except Exception as e:
                print(e)
                pass
            if item['OS']=='freebsd':
                chan = ssh.invoke_shell()
                print(repr(ssh.get_transport()))
                print('*** Here we go!\n')
                stdin, stdout, stderr = ssh.exec_command('/sbin/shutdown -r now', get_pty=True)
                stdin.write(item['password']+'\n')
                for line in stdout:
                    print(line)
            elif item['OS'] in ('unix', 'centos'):
                chan = ssh.invoke_shell()
                print(repr(ssh.get_transport()))
                print('*** Here we go!\n')
                stdin, stdout, stderr = ssh.exec_command('sudo shutdown -r now', get_pty=True)
                stdin.write(item['password'] + '\n')
                for line in stdout:
                    print(line)

            chan.close()
            ssh.close()

        except Exception as excecao:
            pass
            print('*** Caught exception: %s: %s' % (excecao.__class__, excecao))
            traceback.print_exc()
            try:
                ssh.close()
            except:
                pass
            sys.exit(1)
            