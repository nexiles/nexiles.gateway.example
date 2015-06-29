export JAVA_HOME=$(/usr/libexec/java_home -v1.7)
export JYTHON_HOME=$(brew --prefix jython)/libexec

export WT_HOME="$HOME/develop/Windchill/WT_HOME_102"
export IPYTHONDIR="$(pwd)/src/.ipython"
export PYTHONUSERBASE="$(pwd)/src/local"

echo "JAVA_HOME=$JAVA_HOME"
echo "JYTHON_HOME=$JYTHON_HOME"
echo "WT_HOME=$WT_HOME"
echo "IPYTHONDIR=$IPYTHONDIR"
echo "PYTHONUSERBASE=$PYTHONUSERBASE"