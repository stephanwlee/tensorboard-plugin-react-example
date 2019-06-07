echo "Will first build a frontend package using NPM"

pushd tensorboard_plugin_react/frontend
if [ ! -d "node_modules" ]; then
  npm install
else
  echo "node_modules detected. Skipping npm install"
fi
npm run build
popd


echo "Now linking package"
python setup.py develop
echo "Use 'python setup.py develop --uninstall' to remove the plugin."

pushd tensorboard_plugin_react/frontend
npm run watch
popd

