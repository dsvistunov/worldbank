var obj = {
    prop : 'str',
    propSec: 'secstr'
};
var prop;

for (prop in obj) {
    if (obj.hasOwnProperty(prop)) {
        console.log(prop + ' : ' + obj[prop])
    }
}