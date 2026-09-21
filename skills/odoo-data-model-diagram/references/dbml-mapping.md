# Canonical Graph and DBML Mapping

The converter accepts one JSON object:

```json
{
  "title": "Sales model",
  "roots": ["sale.order"],
  "models": [
    {
      "name": "sale.order",
      "label": "Sales Order",
      "module": "sale",
      "auto": true,
      "table": null,
      "inherits": ["mail.thread"],
      "delegates": {"partner_id": "res.partner"},
      "evidence": ["source", "live"],
      "fields": [
        {
          "name": "partner_id",
          "type": "many2one",
          "label": "Customer",
          "relation": "res.partner",
          "inverse": null,
          "required": true,
          "readonly": false,
          "store": true,
          "compute": false,
          "related": false,
          "index": true,
          "selection": [],
          "evidence": ["source", "live"]
        }
      ]
    }
  ]
}
```

Only `title`, `models`, each model `name`, and each field `name`/`type` are
required. Unknown optional fields must be omitted or `null`; do not invent
them. `evidence` values are `source`, `live`, or both.

| Odoo field | DBML type / relation |
| --- | --- |
| `char`, `selection` | `VARCHAR` |
| `text`, `html` | `TEXT` |
| `integer` | `BIGINT` |
| `float` | `FLOAT` |
| `monetary` | `DECIMAL` |
| `boolean` | `BOOLEAN` |
| `date`, `datetime` | `DATE`, `TIMESTAMP` |
| `binary`, `image` | `BLOB` |
| `json`, `properties` | `JSON` |
| `many2one` | `BIGINT` plus a reference |
| `many2many` | synthetic `logical_m2m__...` bridge |
| `one2many` | no column; document the inverse |
| `reference`, `many2one_reference` | `VARCHAR`, no fixed reference |

The converter uses notes for Odoo-only behavior. It does not emit DBML `not
null`, unique, index, or foreign-key delete semantics from ORM metadata alone.
