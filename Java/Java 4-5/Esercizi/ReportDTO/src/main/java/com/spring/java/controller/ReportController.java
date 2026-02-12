package com.spring.java.controller;

import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.java.dto.ProdottoDTO;
import com.spring.java.dto.ProdottoNoIdDTO;
import com.spring.java.dto.ReportDTO;
import com.spring.java.service.ProdottiService;

@RestController
@RequestMapping("/prodotti")
public class ReportController {

    @Autowired
    private ProdottiService prodottiService;

    @PostMapping(consumes = "application/json")
    public void caricaProdotto(@RequestBody ProdottoDTO prodotto) {
        prodottiService.caricaProdotto(prodotto);
    }

    @GetMapping(produces = "application/json")
    public Set<ProdottoNoIdDTO> visualizzaTutti() {
       return prodottiService.visualizzaTutti();
    }

    @GetMapping(path = "/{id}", produces = "application/json")
    public ProdottoDTO visualizzaPerId(@PathVariable int id) {
        return prodottiService.visualizzaPerId(id);
    }

    @GetMapping(path = "/report", produces = "application/json")
    public ReportDTO report() {
        return prodottiService.report();
    }
}
