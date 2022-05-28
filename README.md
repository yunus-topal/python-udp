## docker steps

- server imageı oluştur
    + `docker build -t emretopal20/cmpe492-server .`
- push server image
    + `docker push emretopal20/cmpe492-server 

- client için de aynı şey
    + `docker build -t emretopal20/cmpe492-client .`
    + `docker push emretopal20/cmpe492-client `

## kubernetes steps

- cluster oluştur
   + `k3d cluster create -a 2.`

- server deploymentı oluştur
  + `kubectl apply -f server-deployment.yaml`

- client kodunda server ip adresini ekleyip yeniden build et.

- client deploy et
    + `kubectl apply -f client-deployment.yaml`

## aktarımı görüntüleme

- podun içine girmek için:
    + `kubectl exec --stdin --tty <pod-name> — /bin/bash`
- çalışan python processleri için:
    + `ps -ef | grep python`
- processin console outputunu görmek için:
    + `cat /proc/<pid>/fd/1`

- pod görünlüme:
    + `kubectl get pods -o wide`


