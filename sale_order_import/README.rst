=================
Sale Order Import
=================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:8f06d86294fc834191b72ff6e038d8b5298882b4df0baaf2d0f69699bd6d08cd
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fedi-lightgray.png?logo=github
    :target: https://github.com/OCA/edi/tree/16.0/sale_order_import
    :alt: OCA/edi
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/edi-16-0/edi-16-0-sale_order_import
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/edi&target_branch=16.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module adds support for the import of electronic RFQ or orders. This module provides the base methods to import electronic orders, and you can also plug additional formats by extending the wizard. It requires additional modules to support specific order formats:


* module *sale_order_import_ubl*: adds support for `Universal Business Language (UBL) <http://ubl.xml.org/>`_ RFQs and orders as:

  - XML file,
  - PDF file with an embedded XML file.

**Table of contents**

.. contents::
   :local:

Usage
=====

This module adds a wizard in the sale menu named *Import RFQ or Order*. This wizard will propose you to select the order or RFQ file. Depending on the format of the file (XML or PDF) and the type of file (RFQ or order), it may propose you additional options.

When you import an order, if there is a quotation in Odoo for the same customer, the wizard will propose you to either update the existing quotation or create a new order (in fact, it will create a new quotation, so that you are free to make some modifications before you click on the *Confirm Sale* button to convert the quotation to a sale order).

Once the RFQ/order is imported, you should read the messages in the chatter of the quotation because it may contain important information about the import.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/edi/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/edi/issues/new?body=module:%20sale_order_import%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Akretion
* Camptocamp

Contributors
~~~~~~~~~~~~

* Alexis de Lattre <alexis.delattre@akretion.com>
* Dennis Sluijk <d.sluijk@onestein.nl>
* Andrea Stirpe <a.stirpe@onestein.nl>
* Simone Orsi <simone.orsi@camptocamp.com>
* Duong (Tran Quoc) <duongtq@trobz.com>

Other credits
~~~~~~~~~~~~~

The migration of this module from 13.0 to 16.0 was financially supported by Camptocamp

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/edi <https://github.com/OCA/edi/tree/16.0/sale_order_import>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
