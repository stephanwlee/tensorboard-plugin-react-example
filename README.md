This frontend example is created via [create_react_app](https://facebook.github.io/create-react-app/) with some modification
to disable code-splitting.

To build and locally install this plugin:

```sh
# Please use a new virtualenv
bash ./build.sh
```

and launch modified TensorBoard in the same virtualenv:
```sh
# In the TensorBoard source directory
git fetch https://github.com/stephanwlee/tensorboard.git plugin_rfc_prototype:prototype
git checkout prototype
blaze run tensorboard --logdir [somedir]
```
