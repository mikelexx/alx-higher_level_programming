#!/usr/bin/node
exports.esrever = function (list) {
  const newList = list;
  let left = 0;
  let right = newList.length - 1;
  while (left < right) {
    const tmp = newList[left];
    newList[left] = newList[right];
    newList[right] = tmp;
    left++;
    right--;
  }
  return newList;
};
