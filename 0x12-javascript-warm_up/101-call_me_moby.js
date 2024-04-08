#!/usr/bin/node
module.exports.callMeMoby = (x, func) => {
  for (let count = 0; count < x; count++) {
    func();
  }
};
