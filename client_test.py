import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # checking for each of the quotes that the get data point function calculates he data points correctly
    for quote in quotes:
      # carrying out the assertion
      self.assertEqual(getDataPoint(quote),(quote['stock'],float(quote['top_bid']['price']),float(quote['top_ask']['price']),float(quote['top_bid']['price']+quote['top_ask']['price'])/2))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],float(quote['top_bid']['price']),float(quote['top_ask']['price']),float(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_calculatePriceBidLessThanAsk(self):
    # test for checking if the getDataPoint function works when the ask priceis more than the bid price
    quotes = [
      {'top_ask': {'price': 129.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 131.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],float(quote['top_bid']['price']),float(quote['top_ask']['price']),float(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getRatio_calculateRatioWhenPriceBIsZeroWithoughtConditional(self):
    # if the if statement was not in get ratio this test would pass
    with self.assertRaises(ZeroDivisionError):
      getRatio(5,0)

  def test_getRatio_calculateRatioWhenPriceBIsZeroWithConditional(self):
    #checks that none is returned if price b is 0
    self.assertEqual(getRatio(5,0),None)

  def test_getRatio_calculateRatioWhenPriceAandPriceBIsZero(self):
      # checks that none is returned if price b is 0 and a is 0
      self.assertEqual(getRatio(0, 0), None)

  def test_getRatio_calculateRatioWhenPriceAIsZero(self):
      # checks that none is returned if price b is 0 and a is 0
      self.assertEqual(getRatio(0, 5), 0)

  def test_getRatio_calculateRatio(self):
      # checks that get ratio function works
      self.assertEqual(getRatio(4.34, 5), 4.34/5)
if __name__ == '__main__':
    unittest.main()
