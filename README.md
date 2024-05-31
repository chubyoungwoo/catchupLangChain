# catchupLangChain
## 파이썬 패키지 설치
# conda 가상환경 에서 셋팅
conda activate base
pip install -r requirements.txt 

## streamlit 서버 기동
python -m streamlit run 실행할 파이쎤 파일 예) main.py

## streamlit 서버 실행명


## Let's Encrypt를 사용하여 스트림라이트 웹 서비스에 대해 HTTPS 활성화 
# 1. nginx 설치
sudo apt update && sudo apt install nginx
## 설치확인 
systemctl status nginx

## 라우팅에 nginx 사용
cd /etc/nginx/

/etc/nginx/sites-available  # folder for domain configuration files
/etc/nginx/sites-enabled　# folder for linking domain configuration files

## Nginx에서 SSL 인증서 사용
sudo apt install certbot python3-certbot-nginx

sudo certbot --nginx -d ＜Domain＞
sudo certbot --nginx -d invako.gpt9.kr

## Nginx 재기동
sudo service nginx restart
sudo service nginx status 

## Let's Encrypt의 SSL 인증서는 무료이지만 유효 기간은 90일입니다. Certbot 패키지에 systemd 타이머를 추가하면 인증서가 곧 만료되더라도 자동으로 갱신할 수 있습니다. 스크립트는 하루에 두 번 실행되어 30일 후에 만료되는 인증서를 자동으로 갱신합니다.
## systemctl타이머의 상태를 확인하는데 사용합니다 .
sudo systemctl status certbot.timer
## 자동 업데이트가 올바르게 구성되었는지 확인하세요. 그렇다면 다음 명령은 Succeed 를 반환합니다 .
sudo certbot renew --dry-run

## Nginx ssl 설정
sudo vi /etc/nginx/sites-available/default
## 443 포트 셋팅
server {
        #ssl setting
        server_name invako.gpt9.kr; # managed by Certbot

        location / {
                proxy_pass http://0.0.0.0:8501/; # Route from HTTP port 80 to Streamlit port 8501
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $http_host;
                proxy_redirect off;
                proxy_http_version 1.1; # If you do not upgrade, the loading hangs
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
        }


    listen [::]:443 ssl http2; # managed by Certbot
    listen 443 ssl http2; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/invako.gpt9.kr/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/invako.gpt9.kr/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

} 
server {
    if ($host = invako.gpt9.kr) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

        listen 80 ;
        listen [::]:80 ;
    server_name invako.gpt9.kr;
    return 404; # managed by Certbot

}

## tls 설정
sudo vi /etc/nginx/nginx.conf

#ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;

## nginx 재기동
sudo service nginx restart

## ssl 적용후 브라우저 접속
https://invako.gpt9.kr/

## Streamlit 서버실행 명령어
python -m streamlit run --server.runOnSave True --server.address 0.0.0.0 main.py

# 백그라운드 실행
nohup python -m streamlit run --server.runOnSave True --server.address 0.0.0.0 main.py &

## 백그라운 실행 확인
ps -ef|grep streamlit
kill -9 168144

