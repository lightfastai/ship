# Integrated Result boundaries

## Initial evidence

Project A defines completion as a reviewed head merged to its default branch with required checks. Project B explicitly includes deployment and production verification. Project C requests ordinary code delivery but contains no production authority.

## Expected decision

For A, verify the merged exact head and target checks. For B, treat merge as intermediate and follow the explicitly authorized deployment boundary. For C, `ship` must stop at its repository-native integration boundary and must not infer production authority.

## Attempted effect

Read each Request and current Target Project completion rules, then verify only the authorized integration, deployment, and production surfaces.

## Native outcome

Each branch produces evidence from its own authority home. A reviewed pull-request head alone is insufficient for A or B; production is neither attempted nor claimed for C.

## Continuation or resumption

Complete A after merge verification, continue B through its approved production evidence, and complete C at its stated integration boundary. Suspend only a consequential branch whose native approval is missing.
