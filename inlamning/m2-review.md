# Milstolpe 2 – Branch protection, review och konflikt

## Ruleset

Vi skapade en ruleset för repot som kräver en godkänd pull request innan
ändringar får mergas till main. Enforcement status sattes till Active och
bypass-listan lämnades tom, så regeln gäller alla.

![Ruleset](./imgs/image.png)

## Ny branch

Vi skapade en egen branch per uppgift så att vi kunde arbeta individuellt.

![New branch](./imgs/image-1.png)

## Commit och merge

Varje pull request krävde minst en godkänd review innan den fick mergas
till main. Det andra paret gick igenom ändringarna och godkände dem innan
merge.

![pull request](./imgs/image-2.png)

## Konfliktövningen

Vi skapade en merge-konflikt genom att ändra samma rad, `h1`-rubriken, till BOB på varsin branch.

![bob change](./imgs/image-3.png)

Eftersom samma rad ändrats på båda brancherna gick den senare pull
requesten inte att merga förrän konflikten var löst.

![pr request](./imgs/image-4.png)

Konflikten löstes genom att välja "accept incoming changes": `h1` blev
BOB och konfliktmarkörerna (`<<<<<<<`) togs bort.

![conflict resolving](./imgs/image-5.png)

Pull requesten godkändes och mergades efter att konflikten var löst.

![conflict solved](./imgs/image-6.png)

![alt text](image.png)