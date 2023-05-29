ssh -o StrictHostKeyChecking=no root@$DEV_DO_IP_ADDRESS << 'ENDSSH'
  cd ~/beaver_app
  mkdir -p nginx
  chmod 777 nginx
  export $(cat .env.test | xargs)
  export $(cat .env.test.db | xargs)
  export $(cat .env.test.bkp | xargs)
  docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
  docker pull $IMAGE:app
  docker pull $IMAGE:nginx
  docker pull $IMAGE:rabbit
  docker-compose -f docker-compose.dev.yml up -d
  docker image prune -f
ENDSSH
