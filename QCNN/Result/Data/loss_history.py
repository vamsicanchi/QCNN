import matplotlib.pyplot as plt
import numpy as np
from Benchmarking import Encoding_to_Embedding
from data import data_load_and_process
from Training import circuit_training

# Loss histories in order of pca8, autoencoder8, pca16, autoencoder16
loss_histories_CNN_MNIST = np.array(
    [
        [
            0.714053750038147,
            0.6757248044013977,
            0.6670724749565125,
            0.6759045124053955,
            0.6712536811828613,
            0.6944219470024109,
            0.7101644277572632,
            0.6841925978660583,
            0.6728434562683105,
            0.668999433517456,
            0.6950646042823792,
            0.6684354543685913,
            0.6642752885818481,
            0.666652500629425,
            0.6504575610160828,
            0.6460185050964355,
            0.645703136920929,
            0.6277170181274414,
            0.6505084037780762,
            0.6278526186943054,
            0.6088988184928894,
            0.6650892496109009,
            0.615799605846405,
            0.6277462244033813,
            0.6499466896057129,
            0.615242600440979,
            0.6231257915496826,
            0.5951676368713379,
            0.5982342958450317,
            0.5950978994369507,
            0.5420237183570862,
            0.5638814568519592,
            0.545005202293396,
            0.5448441505432129,
            0.5539039373397827,
            0.5069094300270081,
            0.5558350682258606,
            0.48426052927970886,
            0.5421356558799744,
            0.5551093816757202,
            0.5049896836280823,
            0.4414564371109009,
            0.5025984048843384,
            0.4578346908092499,
            0.4678928256034851,
            0.43783116340637207,
            0.45159730315208435,
            0.4467982351779938,
            0.47169816493988037,
            0.40727710723876953,
            0.4425938129425049,
            0.4238426983356476,
            0.4433065354824066,
            0.4436638355255127,
            0.30902591347694397,
            0.4994756281375885,
            0.4161745011806488,
            0.32217615842819214,
            0.4133518934249878,
            0.32330527901649475,
            0.3460567891597748,
            0.2753203213214874,
            0.4248920679092407,
            0.2533189058303833,
            0.33595219254493713,
            0.31314578652381897,
            0.3584780991077423,
            0.39643460512161255,
            0.36942508816719055,
            0.34632256627082825,
            0.43791523575782776,
            0.2648601233959198,
            0.2459360510110855,
            0.2911376655101776,
            0.3936261832714081,
            0.22703512012958527,
            0.34607556462287903,
            0.22962436079978943,
            0.31266433000564575,
            0.3194691836833954,
            0.3004220128059387,
            0.2597625255584717,
            0.27975985407829285,
            0.3647230863571167,
            0.2021866738796234,
            0.310232013463974,
            0.267425537109375,
            0.20514070987701416,
            0.3879457116127014,
            0.2696777284145355,
            0.20186719298362732,
            0.19994035363197327,
            0.21005916595458984,
            0.20109756290912628,
            0.24811165034770966,
            0.26313042640686035,
            0.21158762276172638,
            0.23533910512924194,
            0.19377802312374115,
            0.26648518443107605,
            0.327722430229187,
            0.4033016860485077,
            0.2014351487159729,
            0.32094427943229675,
            0.35047662258148193,
            0.29127103090286255,
            0.4139123260974884,
            0.4130251705646515,
            0.24823781847953796,
            0.21104803681373596,
            0.306765079498291,
            0.20947876572608948,
            0.17692415416240692,
            0.19715525209903717,
            0.35659322142601013,
            0.1806756854057312,
            0.13031096756458282,
            0.19041313230991364,
            0.18950439989566803,
            0.28686586022377014,
            0.24760431051254272,
            0.2115887999534607,
            0.2320551723241806,
            0.2639220356941223,
            0.26703938841819763,
            0.18723364174365997,
            0.3086016774177551,
            0.0961514264345169,
            0.5094321966171265,
            0.13711600005626678,
            0.12534093856811523,
            0.13913847506046295,
            0.228322371840477,
            0.10770484060049057,
            0.17475208640098572,
            0.15008972585201263,
            0.18664470314979553,
            0.2059953659772873,
            0.1808759719133377,
            0.14071853458881378,
            0.11081507056951523,
            0.21924449503421783,
            0.34293651580810547,
            0.07046297937631607,
            0.08555634319782257,
            0.2753034830093384,
            0.18749330937862396,
            0.09204571694135666,
            0.1777571439743042,
            0.15454773604869843,
            0.30302849411964417,
            0.1936318427324295,
            0.1466241478919983,
            0.10814632475376129,
            0.28570395708084106,
            0.21450716257095337,
            0.2574478089809418,
            0.08683276921510696,
            0.12849056720733643,
            0.23936748504638672,
            0.35046452283859253,
            0.18132348358631134,
            0.06745906174182892,
            0.08519738167524338,
            0.16765129566192627,
            0.1226348802447319,
            0.4494912028312683,
            0.2902643084526062,
            0.14854183793067932,
            0.12457065284252167,
            0.08460919559001923,
            0.165123850107193,
            0.128731831908226,
            0.2893070578575134,
            0.26522427797317505,
            0.14514367282390594,
            0.09648929536342621,
            0.3117218017578125,
            0.2046540230512619,
            0.08452397584915161,
            0.4166283905506134,
            0.2918921709060669,
            0.356248676776886,
            0.3074325621128082,
            0.12465698271989822,
            0.1480899155139923,
            0.24002531170845032,
            0.3299065828323364,
            0.05778765305876732,
            0.18016034364700317,
            0.10325605422258377,
            0.3677785098552704,
            0.07459772378206253,
            0.13220126926898956,
            0.17934730648994446,
            0.07940277457237244,
            0.08888012170791626,
            0.26546308398246765,
            0.4198744595050812,
            0.2377086877822876,
        ],
        [
            0.722859263420105,
            0.721849262714386,
            0.7045133113861084,
            0.7295671105384827,
            0.6710929274559021,
            0.7143537402153015,
            0.6963018178939819,
            0.683974027633667,
            0.7001882791519165,
            0.7011011242866516,
            0.6926947236061096,
            0.6945953369140625,
            0.6880753040313721,
            0.6847305297851562,
            0.6930335760116577,
            0.6383837461471558,
            0.6585142016410828,
            0.6643711924552917,
            0.670865535736084,
            0.6620815992355347,
            0.6525277495384216,
            0.6566925048828125,
            0.6603410840034485,
            0.646219789981842,
            0.6375677585601807,
            0.7443196773529053,
            0.6225131154060364,
            0.653272807598114,
            0.6358342170715332,
            0.681471049785614,
            0.6139385104179382,
            0.6432995796203613,
            0.6474753618240356,
            0.6299405097961426,
            0.6331878900527954,
            0.630324125289917,
            0.6321933269500732,
            0.6136326789855957,
            0.6219558715820312,
            0.6019330024719238,
            0.6050845980644226,
            0.6444574594497681,
            0.6327107548713684,
            0.6075921058654785,
            0.5880964398384094,
            0.5826204419136047,
            0.5313653945922852,
            0.6057491898536682,
            0.6037223935127258,
            0.5866155028343201,
            0.5857460498809814,
            0.5763251781463623,
            0.5990739464759827,
            0.5852251648902893,
            0.5917327404022217,
            0.594275951385498,
            0.5615271329879761,
            0.570615291595459,
            0.4967952072620392,
            0.4958264231681824,
            0.5339020490646362,
            0.5119616985321045,
            0.565489649772644,
            0.5976889729499817,
            0.557020366191864,
            0.5004237294197083,
            0.5867930054664612,
            0.5332251787185669,
            0.6047292947769165,
            0.52519690990448,
            0.5135031342506409,
            0.4499858617782593,
            0.5737566947937012,
            0.537904679775238,
            0.5518447160720825,
            0.5273762345314026,
            0.4588744342327118,
            0.48763972520828247,
            0.4228086471557617,
            0.6082445383071899,
            0.44678717851638794,
            0.5027003288269043,
            0.5093401074409485,
            0.4335576891899109,
            0.6178605556488037,
            0.5808064341545105,
            0.4536117613315582,
            0.46775364875793457,
            0.4472064971923828,
            0.45179107785224915,
            0.452457994222641,
            0.46096116304397583,
            0.4410419464111328,
            0.49289727210998535,
            0.48667240142822266,
            0.5219956040382385,
            0.4383401870727539,
            0.4490739405155182,
            0.43243953585624695,
            0.4779336452484131,
            0.4499213397502899,
            0.4945499002933502,
            0.4267149269580841,
            0.44638243317604065,
            0.3887633979320526,
            0.45998772978782654,
            0.4307110905647278,
            0.349350243806839,
            0.4914915859699249,
            0.39171886444091797,
            0.3926960229873657,
            0.41929078102111816,
            0.3891267478466034,
            0.37243568897247314,
            0.3615072965621948,
            0.3486050069332123,
            0.39569419622421265,
            0.4160010516643524,
            0.395239919424057,
            0.3473738133907318,
            0.3690200746059418,
            0.38260650634765625,
            0.37693727016448975,
            0.35455551743507385,
            0.3153707683086395,
            0.4163806438446045,
            0.33833393454551697,
            0.3445013165473938,
            0.3172437250614166,
            0.2776515483856201,
            0.2830849289894104,
            0.3238430917263031,
            0.39875033497810364,
            0.3399185240268707,
            0.5361736416816711,
            0.41780292987823486,
            0.3610226809978485,
            0.2841382920742035,
            0.3309812545776367,
            0.24294963479042053,
            0.23834404349327087,
            0.2678911089897156,
            0.2697659730911255,
            0.32697904109954834,
            0.37020769715309143,
            0.2873440384864807,
            0.20928901433944702,
            0.35995548963546753,
            0.25920143723487854,
            0.44556766748428345,
            0.2845075726509094,
            0.3141847550868988,
            0.3044743835926056,
            0.32837897539138794,
            0.24346278607845306,
            0.2761305570602417,
            0.2605215013027191,
            0.24642413854599,
            0.3306944966316223,
            0.2538274824619293,
            0.19690634310245514,
            0.2894386947154999,
            0.277312695980072,
            0.2049439549446106,
            0.2273852676153183,
            0.23064839839935303,
            0.2347431629896164,
            0.3478816747665405,
            0.2558739185333252,
            0.22614656388759613,
            0.2866215705871582,
            0.29618847370147705,
            0.2791079580783844,
            0.2986387312412262,
            0.15219609439373016,
            0.2581731081008911,
            0.292522132396698,
            0.24959693849086761,
            0.28260356187820435,
            0.1927589476108551,
            0.18100348114967346,
            0.31418827176094055,
            0.23249584436416626,
            0.3172941505908966,
            0.27895286679267883,
            0.28041180968284607,
            0.24284619092941284,
            0.19051550328731537,
            0.20800790190696716,
            0.23449639976024628,
            0.20080867409706116,
            0.3689790368080139,
            0.1671542525291443,
            0.3172452449798584,
            0.2963358163833618,
            0.17572879791259766,
            0.2509303092956543,
            0.15980759263038635,
            0.2943058907985687,
            0.24765785038471222,
        ],
        [
            0.6766626834869385,
            0.6733847856521606,
            0.7268949747085571,
            0.6916412115097046,
            0.7079758644104004,
            0.6945012807846069,
            0.6860032677650452,
            0.6836898922920227,
            0.6823083758354187,
            0.6946573853492737,
            0.6738471388816833,
            0.7055628299713135,
            0.7074865698814392,
            0.6980187296867371,
            0.6752068996429443,
            0.6878193616867065,
            0.6858772039413452,
            0.6845739483833313,
            0.6781122088432312,
            0.6687148213386536,
            0.6551575660705566,
            0.6618691086769104,
            0.6707185506820679,
            0.6695660948753357,
            0.6733136177062988,
            0.6597137451171875,
            0.6290885806083679,
            0.688670814037323,
            0.6812517642974854,
            0.6421326994895935,
            0.6218180656433105,
            0.6294578313827515,
            0.5880572199821472,
            0.6018733978271484,
            0.6334924101829529,
            0.7113765478134155,
            0.6618599891662598,
            0.6857787370681763,
            0.6958155035972595,
            0.6620758771896362,
            0.6098875999450684,
            0.6351224780082703,
            0.7133780121803284,
            0.6134438514709473,
            0.6188390254974365,
            0.598128080368042,
            0.6313796043395996,
            0.5903613567352295,
            0.6385324001312256,
            0.5774256587028503,
            0.607389509677887,
            0.5639699101448059,
            0.573137104511261,
            0.6269221901893616,
            0.5388535261154175,
            0.5750295519828796,
            0.6302374005317688,
            0.5416637063026428,
            0.5846621990203857,
            0.5884502530097961,
            0.5980594158172607,
            0.6035245656967163,
            0.5252978801727295,
            0.5058540105819702,
            0.4807260036468506,
            0.5133909583091736,
            0.6284927129745483,
            0.5735365152359009,
            0.5716258883476257,
            0.5082230567932129,
            0.5524265766143799,
            0.4895395040512085,
            0.4933544099330902,
            0.5380381345748901,
            0.5306010246276855,
            0.5045926570892334,
            0.5111860036849976,
            0.39580845832824707,
            0.46140849590301514,
            0.40367892384529114,
            0.5849067568778992,
            0.4099409878253937,
            0.46059444546699524,
            0.47587355971336365,
            0.36137184500694275,
            0.4260672330856323,
            0.46819329261779785,
            0.3892982006072998,
            0.4808935821056366,
            0.3398974537849426,
            0.37576550245285034,
            0.34359949827194214,
            0.2874930202960968,
            0.3132879137992859,
            0.3394784927368164,
            0.32755810022354126,
            0.3825659453868866,
            0.4756413400173187,
            0.31717604398727417,
            0.27863574028015137,
            0.3506808578968048,
            0.36046916246414185,
            0.44146835803985596,
            0.3126901090145111,
            0.2787816524505615,
            0.3439459204673767,
            0.37225142121315,
            0.5115729570388794,
            0.3006516695022583,
            0.2852512001991272,
            0.2545645534992218,
            0.38197603821754456,
            0.29596179723739624,
            0.2493038922548294,
            0.4055787920951843,
            0.23028181493282318,
            0.30714738368988037,
            0.24847815930843353,
            0.2578228712081909,
            0.2965392768383026,
            0.2399429827928543,
            0.26306965947151184,
            0.18465633690357208,
            0.2370777726173401,
            0.402022123336792,
            0.2274547517299652,
            0.24400709569454193,
            0.2846790552139282,
            0.2497858852148056,
            0.2619662880897522,
            0.30175483226776123,
            0.22820281982421875,
            0.22678717970848083,
            0.36070916056632996,
            0.31420132517814636,
            0.4352460503578186,
            0.22265543043613434,
            0.34359288215637207,
            0.13647298514842987,
            0.21282663941383362,
            0.21635796129703522,
            0.26533767580986023,
            0.3534102737903595,
            0.32491347193717957,
            0.2294543832540512,
            0.27164843678474426,
            0.19885091483592987,
            0.18760965764522552,
            0.2540241777896881,
            0.4632641077041626,
            0.29165011644363403,
            0.4135802984237671,
            0.26327550411224365,
            0.1997772455215454,
            0.13516023755073547,
            0.3695870637893677,
            0.11264805495738983,
            0.29873695969581604,
            0.16909335553646088,
            0.30733317136764526,
            0.20011112093925476,
            0.18087071180343628,
            0.27615079283714294,
            0.18393971025943756,
            0.5226209163665771,
            0.34045127034187317,
            0.19876118004322052,
            0.1125766783952713,
            0.1594187170267105,
            0.20853376388549805,
            0.1732969880104065,
            0.14923624694347382,
            0.3410123586654663,
            0.3147244155406952,
            0.1611364781856537,
            0.20200948417186737,
            0.3477379083633423,
            0.27802884578704834,
            0.13795316219329834,
            0.18882125616073608,
            0.2493482530117035,
            0.21802087128162384,
            0.08311432600021362,
            0.3638332784175873,
            0.1593743860721588,
            0.12320718169212341,
            0.14631333947181702,
            0.14829546213150024,
            0.12080324441194534,
            0.2866232395172119,
            0.11320976167917252,
            0.1859615445137024,
            0.0962543860077858,
            0.3311655521392822,
            0.22131189703941345,
            0.1387200504541397,
            0.3458332419395447,
            0.2703413665294647,
            0.08891014009714127,
            0.07229170948266983,
        ],
        [
            0.787895917892456,
            0.6903800368309021,
            0.7158403992652893,
            0.7122862339019775,
            0.6886484026908875,
            0.6939958930015564,
            0.6935360431671143,
            0.650316059589386,
            0.6544728875160217,
            0.6994084715843201,
            0.6894413232803345,
            0.6850844621658325,
            0.6804036498069763,
            0.6757852435112,
            0.6671650409698486,
            0.6817684769630432,
            0.6735156178474426,
            0.6615545749664307,
            0.6588905453681946,
            0.645582914352417,
            0.6698077917098999,
            0.6574685573577881,
            0.657529890537262,
            0.6392114758491516,
            0.649583101272583,
            0.6608424186706543,
            0.6229669451713562,
            0.6509481072425842,
            0.6281221508979797,
            0.6040320992469788,
            0.6476627588272095,
            0.6141312718391418,
            0.6132612824440002,
            0.5976462364196777,
            0.5747413039207458,
            0.5883685946464539,
            0.6068240404129028,
            0.5791706442832947,
            0.5358545780181885,
            0.5668087601661682,
            0.5293481945991516,
            0.5469346642494202,
            0.5151075720787048,
            0.48746681213378906,
            0.49674975872039795,
            0.4565601646900177,
            0.4422961175441742,
            0.455774188041687,
            0.4999108910560608,
            0.4826383888721466,
            0.3973392844200134,
            0.4315979480743408,
            0.5005404949188232,
            0.3493035137653351,
            0.40820634365081787,
            0.4267416000366211,
            0.3546534478664398,
            0.29594555497169495,
            0.37569165229797363,
            0.3514409363269806,
            0.39161917567253113,
            0.381989449262619,
            0.35257411003112793,
            0.2563234269618988,
            0.32872822880744934,
            0.3258020281791687,
            0.4029194712638855,
            0.27450475096702576,
            0.29574957489967346,
            0.22943808138370514,
            0.21788370609283447,
            0.1983984112739563,
            0.2505156695842743,
            0.17859338223934174,
            0.19801589846611023,
            0.33501136302948,
            0.2805149555206299,
            0.0791587084531784,
            0.2965260446071625,
            0.09564807265996933,
            0.26017022132873535,
            0.28739306330680847,
            0.39182159304618835,
            0.28442826867103577,
            0.20208536088466644,
            0.20845864713191986,
            0.083095982670784,
            0.11846388131380081,
            0.2296963334083557,
            0.4584989845752716,
            0.2712455689907074,
            0.44045203924179077,
            0.24386362731456757,
            0.25447797775268555,
            0.17673835158348083,
            0.2929280400276184,
            0.2384115606546402,
            0.2909412682056427,
            0.3392401933670044,
            0.19307689368724823,
            0.27072784304618835,
            0.22949834167957306,
            0.09036514163017273,
            0.20298032462596893,
            0.1406632363796234,
            0.1747269630432129,
            0.32058724761009216,
            0.3728943169116974,
            0.3406106233596802,
            0.2329806089401245,
            0.11757044494152069,
            0.10781583189964294,
            0.1772853434085846,
            0.41519486904144287,
            0.2126924693584442,
            0.13533304631710052,
            0.10644836723804474,
            0.22335217893123627,
            0.3297368586063385,
            0.3315538465976715,
            0.43632546067237854,
            0.24056647717952728,
            0.37213650345802307,
            0.16111552715301514,
            0.05763351917266846,
            0.21711736917495728,
            0.13189882040023804,
            0.048426304012537,
            0.14040182530879974,
            0.16238971054553986,
            0.3589114844799042,
            0.12540899217128754,
            0.08508334308862686,
            0.1410427689552307,
            0.18061935901641846,
            0.44160178303718567,
            0.3028709888458252,
            0.07879309356212616,
            0.17187120020389557,
            0.17292766273021698,
            0.22851528227329254,
            0.21786810457706451,
            0.142022967338562,
            0.09644395858049393,
            0.08551015704870224,
            0.33149322867393494,
            0.20092003047466278,
            0.06972720474004745,
            0.20957961678504944,
            0.06169748678803444,
            0.14879749715328217,
            0.2783214747905731,
            0.06366264820098877,
            0.5207465291023254,
            0.16419930756092072,
            0.20410758256912231,
            0.22914914786815643,
            0.1090226098895073,
            0.3697149157524109,
            0.4854496121406555,
            0.15068838000297546,
            0.31723499298095703,
            0.25102636218070984,
            0.23569755256175995,
            0.3954540193080902,
            0.19988884031772614,
            0.0597945898771286,
            0.14768925309181213,
            0.06746945530176163,
            0.11429297178983688,
            0.1333230584859848,
            0.3710431158542633,
            0.13212214410305023,
            0.05055677890777588,
            0.18356674909591675,
            0.2802237272262573,
            0.3557482063770294,
            0.18571825325489044,
            0.2556218206882477,
            0.4787002503871918,
            0.2715683877468109,
            0.13747304677963257,
            0.4504898488521576,
            0.13083931803703308,
            0.22413353621959686,
            0.16070926189422607,
            0.26609182357788086,
            0.14192163944244385,
            0.19613544642925262,
            0.1497608721256256,
            0.2040126472711563,
            0.04195399209856987,
            0.03975365310907364,
            0.580817461013794,
            0.24257855117321014,
            0.3649570047855377,
            0.14266571402549744,
            0.2238038033246994,
            0.3230799734592438,
            0.09331774711608887,
        ],
    ]
)

loss_histories_QCNN_MNIST = np.array([])

loss_histories_TTN_MNIST = np.array([])

loss_histories_CNN_FASHION = np.array([])

loss_histories_QCNN_FASHION = np.array([])

loss_histories_TTN_FASHION = np.array([])


Encodings = ["pca8", "autoencoder8", "pca16-compact", "autoencoder16-compact"]


def plot_loss_history(Encodings, datasets):
    for i in range(len(Encodings)):
        Encoding = Encodings[i]

        if datasets == "mnist":
            loss_history_CNN = loss_histories_CNN_MNIST[i]
            loss_history_QCNN = loss_histories_QCNN_MNIST[i]
            loss_history_TTN = loss_histories_TTN_MNIST[i]
        elif datasets == "fashion":
            loss_history_CNN = loss_histories_CNN_FASHION[i]
            loss_history_QCNN = loss_histories_QCNN_FASHION[i]
            loss_history_TTN = loss_histories_TTN_FASHION[i]

        plt.plot(loss_history_QCNN)
        plt.plot(loss_history_CNN)
        plt.plot(loss_history_TTN)
        plt.title("QCNN vs CNN vs TTN with " + str(Encoding) + " for " + datasets)
        plt.ylabel("loss")
        plt.xlabel("iterations")
        plt.legend(["QCNN", "CNN", "TTN"], loc="upper left")
        plt.show()


datasets = "mnist"
plot_loss_history(Encodings, datasets)
