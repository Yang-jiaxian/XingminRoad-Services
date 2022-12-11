//  -----------------------------------------------------------------------------------------
//  
//  vue: 
//  https://cdnjs.cloudflare.com/ajax/libs/vue/2.5.22/vue.min.js
//
//  smoothscroll polyfill: (disabled)
//  https://cdnjs.cloudflare.com/ajax/libs/iamdustan-smoothscroll/0.4.0/smoothscroll.min.js
//  -----------------------------------------------------------------------------------------

var VueTable = Vue.extend({
    props: ['model'],
    model: {prop: 'model'},
    template: '\n    <table :class="$options._componentTag">\n        <thead>\n            <tr>\n                <th v-for="col in model.head" @click="sort(col.prop)" :class="{ \n                    ascending : prop === col.prop && !reverse,\n                    descending: prop === col.prop && reverse\n                }">{{ col.label }}</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr v-for="row in model.body">\n                <td v-for="col in model.head">{{\xA0row[col.prop]}}</td>\n            </tr>\n        </tbody>\n    </table>\n    ',

    data: function data() {
        return {
            prop: null, // last property used by sort 
            reverse: false // reversed sort order
        };
    },
    mounted: function mounted() {
        //  default sort by first table header (ascending)
        this.sort(this.model.head[0].prop);
    },
    methods: {
        sort: function sort(prop) {
            this.model.body.sort(function (a, b) {
                if (typeof a[prop] === 'number') {
                    return a[prop] - b[prop];
                }
                a = a[prop].toLowerCase();
                b = b[prop].toLowerCase();
                return a < b ? -1 : a > b ? 1 : 0;
            });
            //  flip decscending order if same sort prop or set to false
            //  if descending reverse the data array 
            //  store sort prop
            this.reverse = this.prop === prop ? !this.reverse : false;
            if (this.reverse) this.model.body.reverse();
            this.prop = prop;
            //  Doeas not work in safari
            //  scrollTo(0,0); 
            //  html { scroll-behavior: smooth; }
            //  scroll({ top: 0, left: 0, behavior: 'smooth' });
        }
    }
});
// \ud83d\udd0d
// \uD83D\uDCCC
var data = getData();
var VueApp = new Vue({
    data: data,
    template: '<div id="app"><article>\n            <h1>\ud83d\udcd5 Search Service</h1>\n           <vue-table v-model="data"></vue-table>\n        </article>\n    </div>'
});

Vue.component('vue-table', VueTable);
VueApp.$mount('#app');


function getData() {
    return {
        head: [
            {label: 'Name', prop: 'name', type: 'string'},
            {label: 'Age', prop: 'age', type: 'number'},
            {label: 'Address', prop: 'address', type: 'string'},
            {label: 'City', prop: 'city', type: 'string'},
            {label: 'Ok', prop: 'zip', type: 'string'}],

        body: [
            {
                "name": "Harrison",
                "address": "P.O. Box 984, 7751 Mollis Av.",
                "city": "Vallepietra",
                "zip": "5880",
                "age": 90
            },

            {
                "name": "Grady",
                "address": "171-2694 Sit St.",
                "city": "Calmar",
                "zip": "00499",
                "age": 64
            },

            {
                "name": "Anthony",
                "address": "Ap #216-9083 Accumsan Rd.",
                "city": "Denver",
                "zip": "12230",
                "age": 43
            },

            {
                "name": "Quinn",
                "address": "6514 Eget, St.",
                "city": "Zierikzee",
                "zip": "14170",
                "age": 11
            },

            {
                "name": "Heidi",
                "address": "Ap #663-6617 Pellentesque Av.",
                "city": "Gibbons",
                "zip": "99967-470",
                "age": 62
            },

            {
                "name": "Kiona",
                "address": "187-5861 Condimentum. St.",
                "city": "Schiltigheim",
                "zip": "21911",
                "age": 20
            },

            {
                "name": "Hyatt",
                "address": "399-1710 Et Street",
                "city": "Campagna",
                "zip": "21245",
                "age": 99
            },

            {
                "name": "Rogan",
                "address": "1185 Non Rd.",
                "city": "Segovia",
                "zip": "43028",
                "age": 40
            },

            {
                "name": "Xander",
                "address": "P.O. Box 605, 5724 Pretium Ave",
                "city": "Osasco",
                "zip": "2449 QM",
                "age": 30
            },

            {
                "name": "Katelyn",
                "address": "Ap #431-6354 Lectus. Ave",
                "city": "Cedar Rapids",
                "zip": "99093",
                "age": 70
            },

            {
                "name": "India",
                "address": "675-2715 Ut St.",
                "city": "Attigliano",
                "zip": "9942",
                "age": 73
            },

            {
                "name": "Oscar",
                "address": "3423 Vitae Road",
                "city": "Alajuela",
                "zip": "9478",
                "age": 89
            },

            {
                "name": "Tanek",
                "address": "Ap #154-6658 Tristique Rd.",
                "city": "Buggenhout",
                "zip": "658320",
                "age": 75
            },

            {
                "name": "Jescie",
                "address": "8551 Ad Street",
                "city": "Biarritz",
                "zip": "Y91 0WO",
                "age": 17
            },

            {
                "name": "Honorato",
                "address": "P.O. Box 547, 2597 Curabitur Av.",
                "city": "Pointe-aux-Trembles",
                "zip": "53131",
                "age": 62
            },

            {
                "name": "Aladdin",
                "address": "P.O. Box 901, 6939 Ullamcorper. St.",
                "city": "Sint-Pieters-Woluwe",
                "zip": "7686",
                "age": 43
            },

            {
                "name": "Hasad",
                "address": "Ap #622-7575 Donec Av.",
                "city": "Victoria",
                "zip": "YT40 2ZO",
                "age": 6
            },

            {
                "name": "Tyler",
                "address": "409-801 Malesuada Avenue",
                "city": "Vedrin",
                "zip": "86351",
                "age": 52
            },

            {
                "name": "Gage",
                "address": "584-8560 Ornare, Rd.",
                "city": "Hazaribag",
                "zip": "8085",
                "age": 92
            },

            {
                "name": "Bethany",
                "address": "6522 Et, Road",
                "city": "Kington",
                "zip": "24-005",
                "age": 59
            },

            {
                "name": "Ursula",
                "address": "5212 Massa St.",
                "city": "Leduc",
                "zip": "69549",
                "age": 38
            },

            {
                "name": "Jonas",
                "address": "9497 Commodo Street",
                "city": "Calera de Tango",
                "zip": "63201-171",
                "age": 50
            },

            {
                "name": "Lila",
                "address": "781-2070 Auctor Street",
                "city": "Brandenburg",
                "zip": "79128",
                "age": 96
            },

            {
                "name": "Yuli",
                "address": "Ap #373-3521 Dictum. Rd.",
                "city": "Valparaíso de Goiás",
                "zip": "02077",
                "age": 57
            },

            {
                "name": "Kyla",
                "address": "9513 Commodo Av.",
                "city": "Avernas-le-Bauduin",
                "zip": "2308",
                "age": 26
            },

            {
                "name": "Sebastian",
                "address": "877-300 Adipiscing Rd.",
                "city": "Gillette",
                "zip": "28-991",
                "age": 94
            },

            {
                "name": "Otto",
                "address": "865-9791 Vulputate Avenue",
                "city": "Constitución",
                "zip": "8141",
                "age": 29
            },

            {
                "name": "Yuri",
                "address": "301-4152 Nunc Avenue",
                "city": "Armadale",
                "zip": "63-473",
                "age": 77
            },

            {
                "name": "Willow",
                "address": "P.O. Box 448, 3481 Ultricies Rd.",
                "city": "Kearny",
                "zip": "89994",
                "age": 36
            },

            {
                "name": "Xerxes",
                "address": "P.O. Box 437, 7828 Volutpat. Street",
                "city": "Lions Bay",
                "zip": "4389",
                "age": 43
            },

            {
                "name": "Randall",
                "address": "3160 Dis Rd.",
                "city": "Villers-sur-Semois",
                "zip": "42327",
                "age": 62
            },

            {
                "name": "Elliott",
                "address": "5306 Dui Ave",
                "city": "College",
                "zip": "254003",
                "age": 30
            },

            {
                "name": "Joel",
                "address": "P.O. Box 545, 4339 Tempor Road",
                "city": "Girona",
                "zip": "288513",
                "age": 9
            },

            {
                "name": "Laura",
                "address": "6957 Risus. Ave",
                "city": "My",
                "zip": "6000",
                "age": 99
            },

            {
                "name": "Gil",
                "address": "Ap #697-1422 Scelerisque Street",
                "city": "Papudo",
                "zip": "8731 JN",
                "age": 32
            },

            {
                "name": "Jackson",
                "address": "688-1653 Facilisis Avenue",
                "city": "Rachecourt",
                "zip": "86-069",
                "age": 82
            },

            {
                "name": "Dale",
                "address": "Ap #390-635 Cum St.",
                "city": "Poggio San Marcello",
                "zip": "503979",
                "age": 56
            },

            {
                "name": "Merrill",
                "address": "Ap #435-3256 Risus Street",
                "city": "Gadag Betigeri",
                "zip": "912623",
                "age": 84
            },

            {
                "name": "Candace",
                "address": "Ap #656-7416 Sapien. Rd.",
                "city": "Constitución",
                "zip": "40-696",
                "age": 91
            },

            {
                "name": "Olga",
                "address": "7953 In St.",
                "city": "Stirling",
                "zip": "483558",
                "age": 62
            },

            {
                "name": "Raymond",
                "address": "P.O. Box 785, 6213 Quisque Ave",
                "city": "Nizamabad",
                "zip": "12713",
                "age": 48
            },
            //
            // {
            //     "name": "Karyn",
            //     "address": "9804 Non Rd.",
            //     "city": "Bharuch",
            //     "zip": "J9C 6G4",
            //     "age": 64
            // },
            //
            // {
            //     "name": "Elijah",
            //     "address": "313-572 Sit Rd.",
            //     "city": "Nevers",
            //     "zip": "4294",
            //     "age": 1
            // },
            //
            // {
            //     "name": "Chelsea",
            //     "address": "Ap #395-5889 Pede. Street",
            //     "city": "Rochester",
            //     "zip": "98031",
            //     "age": 33
            // },
            //
            // {
            //     "name": "Baxter",
            //     "address": "9459 Turpis. Road",
            //     "city": "Waarloos",
            //     "zip": "21106",
            //     "age": 68
            // },
            //
            // {
            //     "name": "Tiger",
            //     "address": "125 Aliquam Av.",
            //     "city": "Evesham",
            //     "zip": "14104",
            //     "age": 32
            // },
            //
            // {
            //     "name": "David",
            //     "address": "P.O. Box 460, 4128 Dolor Ave",
            //     "city": "Forchies-la-Marche",
            //     "zip": "89869",
            //     "age": 28
            // },
            //
            // {
            //     "name": "Quinn",
            //     "address": "196-8018 Nulla Rd.",
            //     "city": "Castle Douglas",
            //     "zip": "52061",
            //     "age": 89
            // },
            //
            // {
            //     "name": "Larissa",
            //     "address": "Ap #457-2173 Arcu. Rd.",
            //     "city": "Westende",
            //     "zip": "192263",
            //     "age": 9
            // },
            //
            // {
            //     "name": "Nathan",
            //     "address": "P.O. Box 869, 7154 Euismod St.",
            //     "city": "Jasper",
            //     "zip": "5417 NH",
            //     "age": 70
            // },
            //
            // {
            //     "name": "Emerson",
            //     "address": "Ap #790-6021 Mauris Road",
            //     "city": "Częstochowa",
            //     "zip": "1033",
            //     "age": 95
            // },
            //
            // {
            //     "name": "Margaret",
            //     "address": "Ap #149-2416 Purus. Avenue",
            //     "city": "Bastogne",
            //     "zip": "8834 TZ",
            //     "age": 50
            // },
            //
            // {
            //     "name": "Abel",
            //     "address": "P.O. Box 329, 4526 Sem, Av.",
            //     "city": "Galbiate",
            //     "zip": "895886",
            //     "age": 76
            // },
            //
            // {
            //     "name": "Ashely",
            //     "address": "214-7576 Quam. Street",
            //     "city": "Coalhurst",
            //     "zip": "X87 2DV",
            //     "age": 37
            // },
            //
            // {
            //     "name": "Rylee",
            //     "address": "395 Dapibus Av.",
            //     "city": "Reus",
            //     "zip": "849155",
            //     "age": 87
            // },
            //
            // {
            //     "name": "Desiree",
            //     "address": "821-3088 Maecenas St.",
            //     "city": "Avadi",
            //     "zip": "2421",
            //     "age": 13
            // },
            //
            // {
            //     "name": "Audra",
            //     "address": "902-5605 Fusce Street",
            //     "city": "Merrickville-Wolford",
            //     "zip": "450953",
            //     "age": 98
            // },
            //
            // {
            //     "name": "Eric",
            //     "address": "1335 Ut Street",
            //     "city": "Bruderheim",
            //     "zip": "321726",
            //     "age": 44
            // },
            //
            // {
            //     "name": "Driscoll",
            //     "address": "P.O. Box 883, 4385 Sociis Av.",
            //     "city": "Campitello di Fassa",
            //     "zip": "45137",
            //     "age": 76
            // },
            //
            // {
            //     "name": "Amity",
            //     "address": "P.O. Box 423, 4526 Mollis. St.",
            //     "city": "Montpellier",
            //     "zip": "3082 LC",
            //     "age": 19
            // },
            //
            // {
            //     "name": "Miranda",
            //     "address": "P.O. Box 754, 3232 Dapibus St.",
            //     "city": "Soma",
            //     "zip": "225343",
            //     "age": 64
            // },
            //
            // {
            //     "name": "Allen",
            //     "address": "159-2615 Porttitor Avenue",
            //     "city": "Sherborne",
            //     "zip": "V5R 9K9",
            //     "age": 69
            // },
            //
            // {
            //     "name": "Nathaniel",
            //     "address": "Ap #323-2198 Libero. Rd.",
            //     "city": "Poggio Berni",
            //     "zip": "61519",
            //     "age": 8
            // },
            //
            // {
            //     "name": "Jessamine",
            //     "address": "Ap #949-9997 Tellus. Street",
            //     "city": "Sunderland",
            //     "zip": "M7M 1Z8",
            //     "age": 94
            // },
            //
            // {
            //     "name": "Aubrey",
            //     "address": "9149 Nulla Avenue",
            //     "city": "Paiguano",
            //     "zip": "55543",
            //     "age": 53
            // },
            //
            // {
            //     "name": "Olympia",
            //     "address": "108-5457 Est. Avenue",
            //     "city": "Brucargo",
            //     "zip": "3532 KQ",
            //     "age": 72
            // },
            //
            // {
            //     "name": "Jemima",
            //     "address": "364-8358 Auctor Av.",
            //     "city": "Wekweti",
            //     "zip": "47639",
            //     "age": 18
            // },
            //
            // {
            //     "name": "Dillon",
            //     "address": "Ap #672-2462 Taciti Avenue",
            //     "city": "Issy-les-Moulineaux",
            //     "zip": "9890",
            //     "age": 93
            // },
            //
            // {
            //     "name": "Quintessa",
            //     "address": "674-8671 Laoreet St.",
            //     "city": "Maranello",
            //     "zip": "193239",
            //     "age": 86
            // },
            //
            // {
            //     "name": "Brandon",
            //     "address": "7435 Enim, Ave",
            //     "city": "Yellowhead County",
            //     "zip": "93431",
            //     "age": 82
            // },
            //
            // {
            //     "name": "Aladdin",
            //     "address": "Ap #162-3865 Dolor, Ave",
            //     "city": "Bhilai",
            //     "zip": "5347",
            //     "age": 31
            // },
            //
            // {
            //     "name": "Zelenia",
            //     "address": "P.O. Box 305, 3542 Amet St.",
            //     "city": "Saint-Urbain",
            //     "zip": "36260",
            //     "age": 62
            // },
            //
            // {
            //     "name": "Zenia",
            //     "address": "7958 Lorem Street",
            //     "city": "Stourbridge",
            //     "zip": "N5P 2A8",
            //     "age": 31
            // },
            //
            // {
            //     "name": "Carissa",
            //     "address": "5034 Neque St.",
            //     "city": "Prato Carnico",
            //     "zip": "57-857",
            //     "age": 15
            // },
            //
            // {
            //     "name": "Channing",
            //     "address": "5521 Metus. St.",
            //     "city": "Kota",
            //     "zip": "08-089",
            //     "age": 37
            // },
            //
            // {
            //     "name": "Meredith",
            //     "address": "P.O. Box 927, 449 Hendrerit St.",
            //     "city": "Notre-Dame-de-la-Salette",
            //     "zip": "327920",
            //     "age": 51
            // },
            //
            // {
            //     "name": "Dalton",
            //     "address": "2621 Tristique Av.",
            //     "city": "Blind River",
            //     "zip": "3189 VQ",
            //     "age": 58
            // },
            //
            // {
            //     "name": "Kelsie",
            //     "address": "787-3530 Metus Ave",
            //     "city": "Norcia",
            //     "zip": "03090",
            //     "age": 1
            // },
            //
            // {
            //     "name": "Jana",
            //     "address": "P.O. Box 430, 8910 Fusce Street",
            //     "city": "Fairbanks",
            //     "zip": "1996 DJ",
            //     "age": 33
            // },
            //
            // {
            //     "name": "Laura",
            //     "address": "322-5731 Tellus Ave",
            //     "city": "Poitiers",
            //     "zip": "441315",
            //     "age": 50
            // },
            //
            // {
            //     "name": "Jessamine",
            //     "address": "P.O. Box 992, 6522 At Ave",
            //     "city": "Tumba",
            //     "zip": "23321",
            //     "age": 44
            // },
            //
            // {
            //     "name": "Dolan",
            //     "address": "P.O. Box 906, 8780 Sagittis St.",
            //     "city": "Karnal",
            //     "zip": "200053",
            //     "age": 3
            // },
            //
            // {
            //     "name": "Acton",
            //     "address": "Ap #954-4842 Eget, Street",
            //     "city": "Stekene",
            //     "zip": "1091",
            //     "age": 13
            // },
            //
            // {
            //     "name": "Byron",
            //     "address": "P.O. Box 667, 6982 Eu Ave",
            //     "city": "Offenbach am Main",
            //     "zip": "147775",
            //     "age": 4
            // },
            //
            // {
            //     "name": "Inga",
            //     "address": "3796 Vel Avenue",
            //     "city": "Pimpri-Chinchwad",
            //     "zip": "JT1B 9HE",
            //     "age": 26
            // },
            //
            // {
            //     "name": "Orlando",
            //     "address": "710-4853 Euismod Av.",
            //     "city": "Kapiti",
            //     "zip": "18093-206",
            //     "age": 85
            // },
            //
            // {
            //     "name": "Rogan",
            //     "address": "679-1098 Lorem Road",
            //     "city": "Allumiere",
            //     "zip": "86831-249",
            //     "age": 64
            // },
            //
            // {
            //     "name": "Zane",
            //     "address": "Ap #664-5007 Sem Ave",
            //     "city": "MabomprŽ",
            //     "zip": "6790",
            //     "age": 32
            // },
            //
            // {
            //     "name": "Nasim",
            //     "address": "5489 At, Road",
            //     "city": "Portobuffolè",
            //     "zip": "53808",
            //     "age": 80
            // },
            //
            // {
            //     "name": "Anne",
            //     "address": "2980 Tempus St.",
            //     "city": "Vorselaar",
            //     "zip": "07918",
            //     "age": 55
            // },
            //
            // {
            //     "name": "Jayme",
            //     "address": "958-8261 Vitae Rd.",
            //     "city": "Grande Prairie",
            //     "zip": "21206",
            //     "age": 41
            // },
            //
            // {
            //     "name": "Maia",
            //     "address": "Ap #882-8068 Aliquam St.",
            //     "city": "Meldert",
            //     "zip": "59660",
            //     "age": 77
            // },
            //
            // {
            //     "name": "Sonia",
            //     "address": "Ap #820-5580 Pede St.",
            //     "city": "Cascavel",
            //     "zip": "3906 ZL",
            //     "age": 11
            // },
            //
            // {
            //     "name": "Caryn",
            //     "address": "3834 Aenean Avenue",
            //     "city": "Buckingham",
            //     "zip": "8207",
            //     "age": 48
            // },
            //
            // {
            //     "name": "Colorado",
            //     "address": "1500 Laoreet Street",
            //     "city": "Flin Flon",
            //     "zip": "35301",
            //     "age": 92
            // },
            //
            // {
            //     "name": "Ashton",
            //     "address": "Ap #534-4315 Semper Rd.",
            //     "city": "Chimay",
            //     "zip": "71816-854",
            //     "age": 67
            // },
            //
            // {
            //     "name": "Gabriel",
            //     "address": "6794 Suspendisse St.",
            //     "city": "Casanova Elvo",
            //     "zip": "16-125",
            //     "age": 73
            // },
            //
            // {
            //     "name": "Clare",
            //     "address": "4107 Placerat. Rd.",
            //     "city": "Llanidloes",
            //     "zip": "30215",
            //     "age": 83
            // },

            {
                "name": "Steven",
                "address": "P.O. Box 958, 353 Curabitur Street",
                "city": "Llangefni",
                "zip": "5602",
                "age": 99
            },

            {
                "name": "Celeste",
                "address": "P.O. Box 538, 3563 In Rd.",
                "city": "Medicine Hat",
                "zip": "80-709",
                "age": 99
            }]
    };


}