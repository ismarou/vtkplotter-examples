![vexlogo](https://user-images.githubusercontent.com/32848391/71257028-e70dce00-2332-11ea-88b1-b19d7e4a4c52.png)

Repository for the set of more than 300 examples for [vtkplotter](https://github.com/marcomusy/vtkplotter).
Documentation can be found [**here**](https://vtkplotter.embl.es).

## Download and Install:
```bash
pip install -U git+https://github.com/marcomusy/vtkplotter-examples
```

Or

```bash
git clone https://github.com/marcomusy/vtkplotter-examples
cd vtkplotter-examples
pip install -U .
```
Have any question, or wish to suggest or ask for a missing feature?
Do not hesitate to open a [**issue**](https://github.com/marcomusy/vtkplotter/issues)
or send an [email](mailto:marco.musy@embl.es).


## Run:
Search and run any of the examples with:
```bash
vtkplotter --list
vtkplotter -i -r gyroscope2  # (press spacebar or F1 to exit execution)
```

|     |     |     |     |
|:---:|:---:|:---:|:---:|
| ![gyro](https://user-images.githubusercontent.com/32848391/50738942-687b5780-11d9-11e9-97f0-72bbd63f7d6e.gif) <br>`gyroscope2` | ![thinplate_grid](https://user-images.githubusercontent.com/32848391/51433540-d188b380-1c4c-11e9-81e7-a1cf4642c54b.png ) <br>`thinplate_grid`  | ![trail](https://user-images.githubusercontent.com/32848391/58370826-4aee2680-7f0b-11e9-91e6-3120770cfede.gif) <br>`trail`   | ![quadratic_morphing](https://user-images.githubusercontent.com/32848391/50738890-db380300-11d8-11e9-9cef-4c1276cca334.jpg)  <br>`quadratic_morphing`  |
| ![shrink](https://user-images.githubusercontent.com/32848391/46819143-41042280-cd83-11e8-9492-4f53679887fa.png) <br>`shrink` | ![mesh_custom](https://user-images.githubusercontent.com/32848391/51390972-20d9c180-1b31-11e9-955d-025f1ef24cb7.png) <br>`mesh_custom`   | ![spring](https://user-images.githubusercontent.com/32848391/36788885-e97e80ae-1c8f-11e8-8b8f-ffc43dad1eb1.gif) <br>`spring`   | ![lorenz](https://user-images.githubusercontent.com/32848391/46818115-be7a6380-cd80-11e8-8ffb-60af2631bf71.png) <br>`lorentz`   |
| ![sliders](https://user-images.githubusercontent.com/32848391/50738848-be033480-11d8-11e9-9b1a-c13105423a79.jpg) <br>`sliders` | ![fitspheres1](https://user-images.githubusercontent.com/32848391/50738943-687b5780-11d9-11e9-87a6-054e0fe76241.jpg) <br>`fitspheres1`   | ![fxy](https://user-images.githubusercontent.com/32848391/36611824-fd524fac-18d4-11e8-8c76-d3d1b1bb3954.png) <br>`fxy`   | ![histogram](https://user-images.githubusercontent.com/32848391/68141260-77cc4e00-ff2d-11e9-9280-0efc5b87314d.png) <br>`histogram`   |
| ![boolean](https://user-images.githubusercontent.com/32848391/50738871-c0fe2500-11d8-11e9-8812-442b69be6db9.png) <br>`boolean` | ![brownian2D](https://user-images.githubusercontent.com/32848391/50738948-73ce8300-11d9-11e9-8ef6-fc4f64c4a9ce.gif) <br>`brownian2D`   | ![gas](https://user-images.githubusercontent.com/32848391/50738954-7e891800-11d9-11e9-95aa-67c92ca6476b.gif) <br>`gas`   | ![self_org_maps2d](https://user-images.githubusercontent.com/32848391/54557310-1ade5080-49bb-11e9-9b97-1b53a7689a9b.gif)  <br>`self_org_maps2d`    |
| ![geodesic](https://user-images.githubusercontent.com/32848391/51855637-015f4780-232e-11e9-92ca-053a558e7f70.png)<br>`geodesic` | ![convexHull](https://user-images.githubusercontent.com/32848391/51932732-068cc700-2400-11e9-9b68-30294a4fa4e3.png)  <br>`convexHull`  | ![flatarrow](https://user-images.githubusercontent.com/32848391/54612632-97c00780-4a59-11e9-8532-940c25a5dfd8.png) <br>`flatarrow`   | ![latex](https://user-images.githubusercontent.com/32848391/55568648-6190b200-5700-11e9-9547-0798c588a7a5.png)  <br>`latex`  |
| ![legosurface](https://user-images.githubusercontent.com/32848391/56820682-da40e500-684c-11e9-8ea3-91cbcba24b3a.png)<br>`legosurface`| ![streamlines2](https://user-images.githubusercontent.com/32848391/56964001-9145a500-6b5a-11e9-935b-1b2425bd7dd2.png) <br>`streamlines2`   | ![office](https://user-images.githubusercontent.com/32848391/56964003-9145a500-6b5a-11e9-9d9e-9736d90e1900.png) <br>`office.py`   | ![value-iteration](https://user-images.githubusercontent.com/32848391/56964055-afaba080-6b5a-11e9-99cf-3fac99df9878.jpg)  <br>`value-iteration`  |
| ![shadow](https://user-images.githubusercontent.com/32848391/57312574-1d714280-70ee-11e9-8741-04fc5386d692.png) <br>`shadow`| ![multiple_pendulum](https://user-images.githubusercontent.com/32848391/50738892-db380300-11d8-11e9-807c-fb320c7b7917.gif) <br>`multiple_pend`   | ![interpolateVolume](https://user-images.githubusercontent.com/32848391/59095175-1ec5a300-8918-11e9-8bc0-fd35c8981e2b.jpg) <br>`interpolateVolume`   | ![polarHisto](https://user-images.githubusercontent.com/32848391/64912717-5754f400-d733-11e9-8a1f-612165955f23.png)  <br>`polarHisto`  |
| ![gray_scott](https://user-images.githubusercontent.com/32848391/59788744-aaeaa980-92cc-11e9-825d-58da26ca21ff.gif) | ![donutPlot](https://user-images.githubusercontent.com/32848391/64998178-6f6b7580-d8e3-11e9-9bd8-8dfb9ccd90e4.png)  <br>`donutPlot`  | ![extrude](https://user-images.githubusercontent.com/32848391/65963682-971e1a00-e45b-11e9-9f29-05522ae4a800.png) <br>`extrude`   | ![plotxy](https://user-images.githubusercontent.com/32848391/69158509-d6c1c380-0ae6-11ea-9dbf-ff5cd396a9a6.png) <br>`plotxy`   |
| ![particle_simulator](https://user-images.githubusercontent.com/32848391/50738891-db380300-11d8-11e9-84c2-0f55be7228f1.gif) <br>`particle_simulator`| ![heatconv](https://user-images.githubusercontent.com/32848391/57455107-b200af80-726a-11e9-897d-9c7bcb9854ac.gif) <br>`heatconv` |![elastodynamics](https://user-images.githubusercontent.com/32848391/54932788-bd4a8680-4f1b-11e9-9326-33645171a45e.gif) <br>`elastodynamics`  | ![navier-stokes_lshape](https://user-images.githubusercontent.com/32848391/56671156-6bc91f00-66b4-11e9-8c58-e6b71e2ad1d0.gif)<br>`stokes_lshape`|
