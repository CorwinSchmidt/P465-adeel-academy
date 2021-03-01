import 'package:mongo_dart/mongo_dart.dart';
import 'package:sevr/sevr.dart';

void start() async {
  // log into database
  print("Trying to create database...");
  var db = await Db.create(
      'mongodb+srv://adeelacademy:adeelacademy@cluster0.jegun.mongodb.net/AdeelAcademy?retryWrites=true&w=majority');

  print("Opening...");
  
  await db.open();

  print("opened");

  final coll = db.collection('testCollection');

  print(await coll.find().toList());

  // create server
  const port = 8081;
  final serv = Sevr();
  serv.get('/', [
    (ServRequest req, ServResponse res) async {
      final testCollection = await coll.find().toList();
      return res.status(200).json({'testCollection': testCollection});
    }
  ]);

  serv.post('/', [
    (ServRequest req, ServResponse res) async {
      await coll.save(req.body);
      return res.json(
        await coll.findOne(where.eq('name', req.body['name'])),
      );
    }
  ]);

  // listen for connections on server
  serv.listen(port, callback: () {
    print('server listeining on port: $port');
  });
}
