from collections import OrderedDict

grammar = OrderedDict(
    {
        "Telheader_Quelle": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_source",
        },
        "Telheader_Ziel": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_destination",
        },
        "Telheader_TelSeq": {
            "type": "int",
            "length": 6,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_sequence_number",
        },
        "Telheader_AnlZeit": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_current_datetime",
        },
        "Satzart": {
            "type": "str",
            "length": 9,
            "dp": False,
            "ubl_path": False,
            "df_val": "WEAK00050",
            "df_func": False,
        },
        "RxWeak_WeaId_Mand": {
            "type": "str",
            "length": 3,
            "dp": False,
            "ubl_path": False,
            "df_val": "000",
            "df_func": False,
        },
        "RxWeak_WeaId_WeaNr": {
            "type": "str",
            "length": 20,
            "dp": False,
            "ubl_path": "DespatchAdvice.cbc:ID",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_WeaId_HostWeaKz": {
            "type": "str",
            "length": 5,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "get_source",
        },
        "RxWeak_ExtRef": {
            "type": "str",
            "length": 20,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:OrderReference.cbc:ID",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_WEATYP_Typ": {
            "type": "str",
            "length": 6,
            "dp": False,
            "ubl_path": False,
            "df_val": "STDMAN",
            "df_func": False,
        },
        "RxWeak_LST_Mand": {
            "type": "str",
            "length": 3,
            "dp": False,
            "ubl_path": False,
            "df_val": "000",
            "df_func": False,
        },
        "RxWeak_LST_LiefNr": {
            "type": "str",
            "length": 13,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DespatchSupplierParty."
            "cbc:CustomerAssignedAccountID",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_Name": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "supplier_get_Adrs_Name",
        },
        "RxWeak_Adrs_Name2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "supplier_get_Adrs_Name2",
        },
        "RxWeak_Adrs_Name3": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "supplier_get_Adrs_Name3",
        },
        "RxWeak_Adrs_Name4": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "supplier_get_Adrs_Name4",
        },
        "RxWeak_Adrs_Anrede": {
            "type": "str",
            "length": 15,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DespatchSupplierParty."
            "cac:Party.cac:Contact.cbc:Title",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_Adr": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": "supplier_get_Adrs_Adr",
        },
        "RxWeak_Adrs_Adr2": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_PLZ": {
            "type": "str",
            "length": 10,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DespatchSupplierParty."
            "cac:Party.cac:PostalAddress.cbc:PostalZone",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_Ort": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DespatchSupplierParty."
            "cac:Party.cac:PostalAddress.cbc:CityName",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_OrtTeil": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_Land": {
            "type": "str",
            "length": 4,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DespatchSupplierParty."
            "cac:Party.cac:PostalAddress.cac:Country.cbc:IdentificationCode",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_Tel": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DespatchSupplierParty."
            "cac:Party.cac:Contact.cbc:Telephone",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_Fax": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DespatchSupplierParty."
            "cac:Party.cac:Contact.cbc:Telefax",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_Email": {
            "type": "str",
            "length": 40,
            "dp": False,
            "ubl_path": "DespatchAdvice.cac:DespatchSupplierParty."
            "cac:Party.cac:Contact.cbc:ElectronicMail",
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_WWW": {
            "type": "str",
            "length": 35,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Adrs_ILN": {
            "type": "str",
            "length": 13,
            "dp": False,
            "ubl_path": False,
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_BestTerm": {
            "type": "datetime",
            "length": 14,
            "dp": False,
            "ubl_path": [
                "DespatchAdvice.cac:Shipment.cac:Delivery."
                "cac:PromiseDeliveryPeriod.cbc:EndDate",
                "DespatchAdvice.cac:Shipment.cac:Delivery."
                "cac:PromiseDeliveryPeriod.cbc:EndTime",
            ],
            "df_val": False,
            "df_func": False,
        },
        "RxWeak_Info2Wamas": {
            "type": "str",
            "length": 77,
            "dp": False,
            "ubl_path": "DespatchAdvice.cbc:Note",
            "df_val": False,
            "df_func": False,
        },
    }
)
