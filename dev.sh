echo "Will first build a frontend package using NPM"

pushd tensorboard_plugin_react/frontend
if [ ! -d "node_modules" ]; then
  npm install
else
  echo "node_modules detected. Skipping npm install"
fi
popd


echo "Now linking package"
python setup.py -q develop
echo "Use `python setup.py develop --uninstall` to remove the plugin."

pushd tensorboard_plugin_react/frontend
npm run watch
popd

