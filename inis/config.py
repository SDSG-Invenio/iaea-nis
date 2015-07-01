# -*- coding: utf-8 -*-
import sys

CFG_SITE_LANGS = ["en"]

CFG_SITE_NAME = "INIS Input Management"
CFG_SITE_NAME_INTL = {
    "en": CFG_SITE_NAME
}

DEPOSIT_TYPES = [
    "inis.modules.deposit.workflows.upload:upload",
    "inis.modules.deposit.workflows.book:book",
    "inis.modules.deposit.workflows.audiovisual:audiovisual",
    "inis.modules.deposit.workflows.miscellaneous:miscellaneous",
    "inis.modules.deposit.workflows.report:report",
    "inis.modules.deposit.workflows.patent:patent",
    "inis.modules.deposit.workflows.computer:computer",
]

PACKAGES = [
    "inis.base",
    "inis.demosite",
    "inis.modules.deposit",
    "inis.modules.formatter",
    "inis.modules.stats",
    "invenio.modules.*",
    "invenio.base",
]

try:
    from inis import instance_config
    sys.modules[__name__] = instance_config
    del instance_config
except ImportError:
    pass

CFG_ERROR_MESSAGES = {
    0: 'Fulltext files have names that do not correspond to any known TRN',
    1: 'Files do not contain TTF metadata (or TRN tag "001" is missing)',
    2: 'Wrong country code in TRNs',
    3: 'Duplicated TRNs',
}

CFG_SUMBISSION_ERRORS = {
    0: 'The following fulltext files have names that do not correspond to any known TRN:',
    1: 'The following files do not contain TTF metadata (or TRN tag "001" is missing):',
    2: 'The following TRNs have the wrong country code:',
    3: 'The following TRNs are duplicated (or tag "009" is nor "C" for change record):',
}

CFG_NOTIFY_SUBMISSION = ['d.mironov@iaea.org', 'j.garcia-llopis@iaea.org']

CFG_BIBINDEX_PATH_TO_STOPWORDS_FILE = "etc/bibrank/stopwords.kb"

CFG_OAI_METADATA_FORMATS = {
    'oai_dc': ('XOAIDC', 'http://www.openarchives.org/OAI/1.1/dc.xsd',
                         'http://purl.org/dc/elements/1.1/'),
    'oai_ttf': ('XOAITTF', '', ''),
    'marcxml': ('XOAIMARC',
                'http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd',
                'http://www.loc.gov/MARC21/slim'),
    }

CFG_COUNTRIES_DICT = {
    'AD': 'Andorra',
    'AE': 'United Arab Emirates',
    'AF': 'Afghanistan',
    'AG': 'Antigua and Barbuda',
    'AL': 'Albania',
    'AM': 'Armenia',
    'AO': 'Angola',
    'AR': 'Argentina',
    'AT': 'Austria',
    'AU': 'Australia',
    'AX': 'Aland Islands',
    'AZ': 'Azerbaijan',
    'BA': 'Bosnia and Herzegovina',
    'BB': 'Barbados',
    'BD': 'Bangladesh',
    'BE': 'Belgium',
    'BF': 'Burkina Faso',
    'BG': 'Bulgaria',
    'BH': 'Bahrain',
    'BI': 'Burundi',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BN': 'Brunei Darussalam',
    'BO': 'Bolivia, Plurinational State of',
    'BR': 'Brazil',
    'BS': 'Bahamas',
    'BT': 'Bhutan',
    'BW': 'Botswana',
    'BY': 'Belarus',
    'BZ': 'Belize',
    'CA': 'Canada',
    'CD': 'Congo, The Democratic Republic of the',
    'CF': 'Central African Republic',
    'CH': 'Switzerland',
    'CI': "Cote d'Ivoire",
    'CL': 'Chile',
    'CM': 'Cameroon',
    'CN': 'China',
    'CO': 'Colombia',
    'CR': 'Costa Rica',
    'CU': 'Cuba',
    'CV': 'Cape Verde',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DD': 'German Democratic Republic',
    'DE': 'Germany',
    'DJ': 'Djibouti',
    'DK': 'Denmark',
    'DM': 'Dominica',
    'DO': 'Dominican Republic',
    'DZ': 'Algeria',
    'EC': 'Ecuador',
    'EE': 'Estonia',
    'EG': 'Egypt',
    'ER': 'Eritrea',
    'ES': 'Spain',
    'ET': 'Ethiopia',
    'FI': 'Finland',
    'FJ': 'Fiji',
    'FO': 'Faroe Islands',
    'FR': 'France',
    'GA': 'Gabon',
    'GB': 'United Kingdom',
    'GD': 'Grenada',
    'GE': 'Georgia',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GM': 'Gambia',
    'GN': 'Guinea',
    'GQ': 'Equatorial Guinea',
    'GR': 'Greece',
    'GT': 'Guatemala',
    'GU': 'Guam',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HK': 'Hong Kong',
    'HN': 'Honduras',
    'HR': 'Croatia',
    'HT': 'Haiti',
    'HU': 'Hungary',
    'ID': 'Indonesia',
    'IE': 'Ireland',
    'IL': 'Israel',
    'IN': 'India',
    'IQ': 'Iraq',
    'IR': 'Iran, Islamic Republic of',
    'IS': 'Iceland',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JO': 'Jordan',
    'JP': 'Japan',
    'KE': 'Kenya',
    'KG': 'Kyrgyzstan',
    'KH': 'Cambodia',
    'KI': 'Kiribati',
    'KM': 'Comoros',
    'KN': 'Saint Kitts and Nevis',
    'KP': "Korea, Democratic People's Republic of",
    'KR': 'Korea, Republic of',
    'KW': 'Kuwait',
    'KY': 'Cayman Islands',
    'KZ': 'Kazakhstan',
    'LA': "Lao People's Democratic Republic",
    'LB': 'Lebanon',
    'LC': 'Saint Lucia',
    'LI': 'Liechtenstein',
    'LK': 'Sri Lanka',
    'LR': 'Liberia',
    'LS': 'Lesotho',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'LY': 'Libya',
    'MA': 'Morocco',
    'MC': 'Monaco',
    'MD': 'Moldova, Republic of',
    'ME': 'Montenegro',
    'MG': 'Madagascar',
    'MH': 'Marshall Islands',
    'MK': 'Macedonia (FYROM)',
    'ML': 'Mali',
    'MM': 'Myanmar',
    'MN': 'Mongolia',
    'MO': 'Macao',
    'MR': 'Mauritania, Islamic Republic of',
    'MT': 'Malta',
    'MU': 'Mauritius',
    'MV': 'Maldives',
    'MW': 'Malawi',
    'MX': 'Mexico',
    'MY': 'Malaysia',
    'MZ': 'Mozambique',
    'NA': 'Namibia',
    'NC': 'New Caledonia',
    'NE': 'Niger',
    'NG': 'Nigeria',
    'NI': 'Nicaragua',
    'NL': 'Netherlands',
    'NO': 'Norway',
    'NP': 'Nepal',
    'NR': 'Nauru',
    'NU': 'Niue',
    'NZ': 'New Zealand',
    'OM': 'Oman',
    'PA': 'Panama',
    'PE': 'Peru',
    'PG': 'Papua New Guinea',
    'PH': 'Philippines',
    'PK': 'Pakistan',
    'PL': 'Poland',
    'PR': 'Puerto Rico',
    'PS': 'Palestinian Territory, Occupied',
    'PT': 'Portugal',
    'PW': 'Palau',
    'PY': 'Paraguay',
    'QA': 'Qatar',
    'RO': 'Romania',
    'RS': 'Serbia',
    'RU': 'Russian Federation',
    'RW': 'Rwanda',
    'SA': 'Saudi Arabia',
    'SB': 'Solomon Islands',
    'SC': 'Seychelles',
    'SD': 'Sudan',
    'SE': 'Sweden',
    'SG': 'Singapore',
    'SI': 'Slovenia',
    'SK': 'Slovakia',
    'SL': 'Sierra Leone',
    'SM': 'San Marino',
    'SN': 'Senegal',
    'SO': 'Somalia',
    'SR': 'Suriname',
    'ST': 'Sao Tome and Principe',
    'SU': 'USSR',
    'SV': 'El Salvador',
    'SY': 'Syrian Arab Republic',
    'SZ': 'Swaziland',
    'TD': 'Chad',
    'TG': 'Togo',
    'TH': 'Thailand',
    'TJ': 'Tajikistan',
    'TM': 'Turkmenistan',
    'TN': 'Tunisia',
    'TO': 'Tonga',
    'TR': 'Turkey',
    'TT': 'Trinidad and Tobago',
    'TV': 'Tuvalu',
    'TZ': 'Tanzania, United Republic of',
    'UA': 'Ukraine',
    'UG': 'Uganda',
    'US': 'United States',
    'UY': 'Uruguay',
    'UZ': 'Uzbekistan',
    'VA': 'Vatican City State, Holy See',
    'VC': 'Saint Vincent and the Grenadines',
    'VE': 'Venezuela, Bolivarian Republic of',
    'VN': 'Viet Nam',
    'VU': 'Vanuatu',
    'WS': 'Samoa',
    'YE': 'Yemen',
    'YU': 'Yugoslavia',
    'ZA': 'South Africa',
    'ZM': 'Zambia',
    'ZW': 'Zimbabwe',
    'ZZ': 'Country Unknown',
}

CFG_ORGANIZATIONS_DICT = {
    'AA': 'International Organisation without Location',
    'EP': 'European Patent Office',
    'QM': 'World Nuclear Association (WNA)',
    'QN': 'World Nuclear University (WNU)',
    'QP': 'Brazilian-Argentine Agency for Accounting and Control of Nuclear Materials (ABACC)',
    'QQ': 'Middle Eastern Radioisotope Centre for the Arab Countries (MERRCAC)',
    'QR': 'Synchrotron-light for Experimental Science and Applications in the Middle East (SESAME)',
    'QS': 'Information Service in Physics, Electrotechnology and Control (INSPEC)',
    'QZ': 'International Patent Document Centre (INPADOC)',
    'WO': 'World Intellectual Property Organization (WIPO)',
    'XA': 'International Atomic Energy Agency (IAEA)',
    'XB': 'United Nations Scientific Committee on the Effects of Atomic Radiation (UNSCEAR)',
    'XC': 'European Organization for Nuclear Research (CERN)',
    'XD': 'Organization for Economic Co-Operation and Development (OECD)',
    'XE': 'European Commission (EC)',
    'XF': 'Food and Agriculture Organization of the United Nations (FAO)',
    'XG': 'International Committee for Future Accelerators',
    'XH': 'Arab Atomic Energy Agency (AAEA)',
    'XI': 'International Institute for Applied Systems Analysis (IIASA)',
    'XJ': 'Joint Institute for Nuclear Research (JINR)',
    'XK': 'World Meteorological Organization (WMO)',
    'XM': 'International Centre for Scientific and Technical Information (ICSTI)',
    'XN': 'Nuclear Energy Agency of the OECD (NEA)',
    'XO': 'African Union (OAU)',
    'XP': 'Organization of the Petroleum Exporting Countries (OPEC)',
    'XQ': 'Comprehensive Nuclear-Test-Ban Treaty Organization (CTBTO)',
    'XR': 'International Commission on Radiological Protection (ICRP)',
    'XS': 'International Organization for Standardization (ISO)',
    'XT': 'United Nations Industrial Development Organisation (UNIDO)',
    'XU': 'United Nations (UN)',
    'XV': 'World Council of Nuclear Workers (WONUC)',
    'XW': 'World Health Organization (WHO)',
    'XX': 'World Energy Council (WEC)',
    'XY': 'International Energy Agency (IEA)',
    'XZ': 'European Space Agency (ESA)',
}

CFG_MEMBERS_DICT = {}
CFG_MEMBERS_DICT.update(CFG_ORGANIZATIONS_DICT)
CFG_MEMBERS_DICT.update(CFG_COUNTRIES_DICT)

CFG_MEMBERS_NAMES = CFG_MEMBERS_DICT.values()
CFG_MEMBERS_NAMES.sort()

CFG_MEMBERS_CODES = CFG_MEMBERS_DICT.keys()
CFG_MEMBERS_CODES.sort()

CFG_MEMBERS_INV = {v: k for k, v in CFG_MEMBERS_DICT.items()}

CFG_ILOS = [
    {'country': CFG_MEMBERS_DICT['XA'], 'name': 'Alexander Anastassov', 'email': 'a.Anastassov@iaea.org'},
    {'country': CFG_MEMBERS_DICT['ES'], 'name': 'Jaime García', 'email': 'j.garcia-llopis@iaea.org'},
]

CFG_MONTH_CODES = [
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December'),
]
CFG_SEASON_CODES = [
    ('Spr', 'Spring'),
    ('Sum', 'Summer'),
    ('Aut', 'Autum'),
    ('Win', 'Winter'),
]

CFG_LANG_CODES = {
    'AF': 'Afrikaans',
    'AL': 'Albanian',
    'AM': 'Amharic',
    'AR': 'Arabic',
    'AZ': 'Azerbaijani',
    'BE': 'Byelorussian',
    'BG': 'Bulgarian',
    'CS': 'Czech',
    'CY': 'Welsh',
    'DA': 'Danish',
    'DE': 'German',
    'EL': 'Greek',
    'EN': 'English',
    'ES': 'Spanish',
    'ET': 'Estonian',
    'FA': 'Persian',
    'FI': 'Finnish',
    'FR': 'French',
    'GA': 'Irish',
    'HI': 'Hindi',
    'HR': 'Croatian',
    'HU': 'Hungarian',
    'HY': 'Armenian',
    'IN': 'Indonesian',
    'IT': 'Italian',
    'IW': 'Hebrew',
    'JA': 'Japanese',
    'KA': 'Georgian',
    'KK': 'Kazak',
    'KO': 'Korean',
    'KY': 'Kirghiz',
    'LT': 'Lithuanian',
    'LV': 'Latvian',
    'MK': 'Macedonian',
    'MN': 'Mongolian',
    'MO': 'Moldavian',
    'MS': 'Malay',
    'MY': 'Burmese',
    'NL': 'Dutch',
    'NO': 'Norwegian',
    'PL': 'Polish',
    'PT': 'Portuguese',
    'RO': 'Romanian',
    'RU': 'Russian',
    'SH': 'Serbo-Croat',
    'SK': 'Slovak',
    'SL': 'Slovenian',
    'SR': 'Serbian',
    'SV': 'Swedish',
    'TG': 'Tajik',
    'TH': 'Thai',
    'TK': 'Turkmen',
    'TR': 'Turkish',
    'UK': 'Ukrainian',
    'UZ': 'Uzbek',
    'VI': 'Vietnamese',
    'ZH': 'Chinese',
}
