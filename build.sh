echo "Will first build a frontend package using NPM"
pushd tensorboard_plugin_react/frontend
npm install
npm run build
popd

echo "Now building pip"
python setup.py bdist_wheel --python-tag py2 

# optional
pip install dist/tensorboard_plugin_react-0.0.1-py2-none-any.whl -U
