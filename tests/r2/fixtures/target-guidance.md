# Parcel Demo project instructions

This small fixture represents a separate target project, not the AFR authoring repository.

- Preserve Python 3.10 support and use the standard library only.
- The structured status values and CLI exit codes are public compatibility contracts; human-readable labels are separate.
- Specifications under `specs/` are authoritative for their named changes. A specification can depend on a separately owned policy document.
- Keep a sufficient existing specification as the planning source. Write a new plan file only when requested.
- Changes to data visibility or access policy need the policy owner's decision; implementation convenience is not policy authority.
