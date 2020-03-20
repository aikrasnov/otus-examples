#sed -e "s|@@BASE_IMAGE@@|ubuntu|g" < "dockerfile.tmpl" > "./Dockerfile"
sed -e "s|@@BASE_IMAGE@@|$1|g" < "dockerfile.tmpl" > "./Dockerfile"
