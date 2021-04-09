#   LookWell v0.0
#srl

from lookwell import ItemList, Mill

def get_list0():
		list = ItemList({
		items: [
			{
				tags:[ "upc/0001", "food/organic/apple"],
				desc:"2# bag of fuji apple",
				unit:{
				   unit:"pound",
				   qty:2,
				   container:"bag"
				},
			}
		]
	})
	return list


@Test
def test_itemlist():
	list = get_list0()
	assert list is not None
	item = list.findByTag("upc/0001")
	assert item is not None
	assert item.unitstr() == "2 pound bag"


@Test
def test_mill():
	mill = Mill(get_list0())
	assert mill.qtyByTag('upc/0001') is None
	mill.process({
		"date":"2021-03-01"
	})
	assert mill.qtyByTag('upc/0001') is None
	mill.process({
		"buy":{
			tag: "upc/0001",
			qty:2,
		}
	})
	assert mill.qtyByTag("upc/0001").getInUnit("pound") == 4
	mill.process({
		"date":"2021-03-02",
		"census": [
			{ tag:"upc/0001",
				qty:{ unit:"each", qty:9 } } ] })
	assert mill.qtyByTag("upc/001").getInUnit("each") == 9
	mill.process({
		"date":"2021-03-03",
		"eat": [
			{ tag:"upc/0001",
				qty:{ unit:"each", qty:2 } } ] })
	assert mill.qtyByTag("upc/001").getInUnit("each") == 7
	
	
